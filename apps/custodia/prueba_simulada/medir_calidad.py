import subprocess, numpy as np, sys
from PIL import Image
def stats(path):
    out=[]
    for i in range(16):
        t=15*(i+.5)/16
        raw=subprocess.run(['ffmpeg','-loglevel','error','-ss',str(t),'-i',path,'-frames:v','1','-vf','scale=160:-1','-f','rawvideo','-pix_fmt','rgb24','-'],capture_output=True).stdout
        a=np.frombuffer(raw,np.uint8).reshape(-1,160,3).astype(float)
        g=.299*a[...,0]+.587*a[...,1]+.114*a[...,2]
        l=4*g[1:-1,1:-1]-g[:-2,1:-1]-g[2:,1:-1]-g[1:-1,:-2]-g[1:-1,2:]
        out.append((l.var(),g.mean()))
    s=sorted(x[0] for x in out);return round(s[len(s)//2]),round(np.mean([x[1] for x in out]))
for v in sys.argv[1:]:
    sh,br=stats(v);print(f'{v:28s} nitidez(mediana)={sh:5d}  brillo={br:4d}')
