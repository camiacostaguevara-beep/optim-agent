# Genera envíos ficticios (videos de 15 s y fotos de admisión) para probar el reconocimiento.
import numpy as np, subprocess, os, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
F='/usr/share/fonts/truetype/dejavu/'
def font(n,s): return ImageFont.truetype(F+n,s)
rng=np.random.default_rng(7)

def noise(img,amt):
    a=np.asarray(img).astype(np.int16); a=a+rng.integers(-amt,amt+1,a.shape); return Image.fromarray(np.clip(a,0,255).astype(np.uint8))

def face(kind):
    W,H=900,640
    if kind in('A','B'):
        im=noise(Image.new('RGB',(W,H),(196,160,112)),14); d=ImageDraw.Draw(im)
        d.rectangle([0,280,W,340],fill=(40,90,200))                      # cinta azul
        d.text((40,40),'VELOZ',font=font('DejaVuSans-Bold.ttf',70),fill=(200,30,30))
        d.text((44,115),'EXPRESS',font=font('DejaVuSans-Bold.ttf',34),fill=(200,30,30))
        d.polygon([(330,60),(380,40),(380,120)],fill=(200,30,30))         # logo flecha
        lab=(255,255,255) if kind=='A' else (250,225,80)
        d.rectangle([470,380,860,610],fill=lab,outline=(30,30,30),width=3)
        g='700123456789' if kind=='A' else '700123456788'
        d.text((490,395),'GUÍA',font=font('DejaVuSans.ttf',22),fill=(0,0,0))
        d.text((490,420),g,font=font('DejaVuSansMono.ttf',40),fill=(0,0,0))
        x=490
        for i,c in enumerate(g*3):
            w=1+int(c)%3; d.rectangle([x,475,x+w,520],fill=(0,0,0)); x+=w+2
        d.text((490,530),'DESTINO: MEDELLÍN',font=font('DejaVuSans-Bold.ttf',24),fill=(0,0,0))
        d.text((490,565),'Rem.: Ana Pérez · Bogotá',font=font('DejaVuSans.ttf',20),fill=(0,0,0))
        if kind=='A':
            d.text((60,420),'FRÁGIL',font=font('DejaVuSerif-Bold.ttf',46),fill=(20,20,20))  # escrito a mano
            d.polygon([(W-120,0),(W,0),(W,110)],fill=(120,90,55))                         # esquina aplastada
    else:
        im=noise(Image.new('RGB',(W,H),(225,228,232)),8); d=ImageDraw.Draw(im)
        for y in range(0,H,40): d.line([(0,y),(W,y+25)],fill=(205,208,214),width=6)        # pliegues de la bolsa
        d.ellipse([40,40,170,170],fill=(30,140,70))
        d.text((190,60),'MENSAJERÍA',font=font('DejaVuSans-Bold.ttf',48),fill=(30,140,70))
        d.text((190,115),'ANDINA',font=font('DejaVuSans-Bold.ttf',48),fill=(30,140,70))
        d.rectangle([470,380,860,610],fill=(255,255,255),outline=(30,30,30),width=3)
        d.text((490,395),'GUÍA',font=font('DejaVuSans.ttf',22),fill=(0,0,0))
        d.text((490,420),'700987654321',font=font('DejaVuSansMono.ttf',40),fill=(0,0,0))
        d.text((490,530),'DESTINO: CALI',font=font('DejaVuSans-Bold.ttf',24),fill=(0,0,0))
    return im

def persp_coeffs(src,dst):
    A=[];B=[]
    for (x,y),(X,Y) in zip(dst,src):
        A.append([x,y,1,0,0,0,-X*x,-X*y]);B.append(X)
        A.append([0,0,0,x,y,1,-Y*x,-Y*y]);B.append(Y)
    return np.linalg.solve(np.array(A,float),np.array(B,float)).tolist()

def scene(fc,yaw,zoom,cx,cy,bright,warm,blur,shake):
    W,H=1280,720
    bg=noise(Image.new('RGB',(W,H),(110,112,115)),10)
    fw,fh=fc.size; s=0.62*zoom; w=fw*s*np.cos(yaw); h=fh*s
    x0=W/2-w/2+cx; y0=H/2-h/2+cy; k=h*0.12*np.sin(yaw)
    dst=[(x0,y0+(k if yaw>0 else 0)),(x0+w,y0+(0 if yaw>0 else -k)),(x0+w,y0+h-(0 if yaw>0 else -k)),(x0,y0+h-(k if yaw>0 else 0))]
    src=[(0,0),(fw,0),(fw,fh),(0,fh)]
    warped=fc.transform((W,H),Image.PERSPECTIVE,persp_coeffs(src,dst),Image.BICUBIC)
    mask=Image.new('L',fc.size,255).transform((W,H),Image.PERSPECTIVE,persp_coeffs(src,dst))
    bg.paste(warped,(0,0),mask)
    if shake: bg=bg.rotate(float(rng.normal(0,2.5)),resample=Image.BICUBIC,fillcolor=(110,112,115))
    if blur: bg=bg.filter(ImageFilter.GaussianBlur(blur))
    bg=ImageEnhance.Brightness(bg).enhance(bright)
    if warm:
        a=np.asarray(bg).astype(float); a[...,0]*=1.08; a[...,2]*=0.86; bg=Image.fromarray(np.clip(a,0,255).astype(np.uint8))
    return noise(bg,6)

def video(name,kind,bright=1.0,warm=False,blur=0.0,shake=False,phase=0.0):
    fc=face(kind); os.makedirs('fr',exist_ok=True); n=15*15
    for i in range(n):
        t=i/n
        yaw=0.9*np.sin(2*np.pi*(t+phase))             # da la vuelta al paquete
        zoom=1.0+ (1.1 if 0.5<t<0.72 else 0.0)        # se acerca a la etiqueta
        cx,cy=(-330,-130) if 0.5<t<0.72 else (0,0)
        b=blur+(rng.uniform(0,3) if shake else (2.5 if i%17==0 else 0))   # algunos cuadros movidos
        scene(fc,yaw,zoom,cx,cy,bright,warm,b,shake).save(f'fr/{i:04d}.jpg',quality=88)
    subprocess.run(['ffmpeg','-loglevel','error','-y','-framerate','15','-i','fr/%04d.jpg','-c:v','libvpx','-b:v','2M',name+'.webm'],check=True)
    subprocess.run('rm -rf fr',shell=True)

def photos(kind):
    fc=face(kind)
    for j,(yaw,z) in enumerate([(0.0,1.0),(0.5,1.0),(0.0,1.9)]):
        cx,cy=((-300,-120) if z>1.5 else (0,0))
        scene(fc,yaw,z,cx,cy,1.0,False,0,False).save(f'adm_{kind}_{j}.jpg',quality=90)

for k in 'ABC': photos(k)
video('custodia_A_ok','A',bright=0.85,warm=True,phase=0.3)
video('custodia_A_movido','A',shake=True,blur=2.0,phase=0.1)
video('custodia_A_oscuro','A',bright=0.22,phase=0.2)
video('custodia_B_ok','B',bright=0.9,phase=0.15)
print(sorted(os.listdir('.')))
