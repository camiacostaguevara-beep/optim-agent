import numpy as np,subprocess,os
src=open('generar_envios.py').read().split("for k in 'ABC'")[0]
exec(src)
from PIL import Image
A=face('A').resize((300,213));C=face('C').resize((260,185));B0=Image.new('RGB',(240,170),(150,118,80))
os.makedirs('fc',exist_ok=True);fps=5;n=60*fps
for i in range(n):
    t=i/fps
    bg=noise(Image.new('RGB',(1280,720),(95,98,100)),8)
    d=ImageDraw.Draw(bg);d.rectangle([0,430,1280,520],fill=(60,62,64))          # banda transportadora
    bg.paste(C,(80,180));bg.paste(B0,(980,170))                                   # cajas quietas
    if 20<=t<=35:x=int(-300+(t-20)/15*1600);bg.paste(A,(x,330))                  # el paquete A pasa por la banda
    bg=bg.filter(ImageFilter.GaussianBlur(1.2));bg=ImageEnhance.Brightness(bg).enhance(0.8)
    noise(bg,10).save(f'fc/{i:04d}.jpg',quality=70)
subprocess.run(['ffmpeg','-loglevel','error','-y','-framerate',str(fps),'-i','fc/%04d.jpg','-c:v','libvpx','-b:v','1M','cctv.webm'],check=True)
subprocess.run('rm -rf fc',shell=True);print('ok')
