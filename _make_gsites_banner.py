from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

OUT = Path(r'C:\Users\USER\Downloads\KIACreative_Products\Landing_Page\Google_Sites_Banner_1600x600.png')
W, H = 1600, 600
PINE = (26,46,38); CREAM = (243,240,229); GOLD = (199,165,97)
FB = r'C:\Windows\Fonts\arialbd.ttf'; FR = r'C:\Windows\Fonts\arial.ttf'

im = Image.new('RGB',(W,H),PINE)
d = ImageDraw.Draw(im,'RGBA')
# subtle diagonal glow
for i in range(0,300,4):
    d.line([(W-i,0),(W-i-300,H)],fill=GOLD+(int(12*(1-i/300)),),width=4)
d.rectangle([0,0,W,10],fill=GOLD+(255,))
d.rectangle([0,H-10,W,H],fill=GOLD+(255,))
d.text((90,120),'KIACREATIVE',font=ImageFont.truetype(FB,104),fill=CREAM+(255,))
d.text((95,250),'DIGITAL PRODUCTS FOR SMALL BUSINESSES',font=ImageFont.truetype(FR,40),fill=GOLD+(255,))
d.line([(95,340),(700,340)],fill=GOLD+(255,),width=3)
d.text((95,400),'Templates  ·  Web apps  ·  Printables  ·  AI skills',font=ImageFont.truetype(FR,32),fill=CREAM+(210,))
d.rounded_rectangle([1240,120,1510,200],radius=30,fill=GOLD+(255,))
d.text((1375,160),'SHOP ALL ↗',font=ImageFont.truetype(FB,30),fill=PINE+(255,),anchor='mm')
d.text((1375,250),'kiacreative.etsy.com',font=ImageFont.truetype(FR,24),fill=CREAM+(255,),anchor='mm')
d.text((1375,300),'adzcute.gumroad.com',font=ImageFont.truetype(FR,24),fill=CREAM+(255,),anchor='mm')
im.save(OUT,optimize=True)
print(OUT, im.size, round(OUT.stat().st_size/1024,1),'KB')
