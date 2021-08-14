from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from resizeimage import resizeimage

bname=input("Enter Name : ")
bdate=input("Enter Date : ")
bpic=input("Enter image path : ")
bdate=(f"({bdate})")
# fd_img = open('pic.jpg', 'r')
img=Image.open(bpic)
img=resizeimage.resize_thumbnail(img, [1120, 3000])
img.save('.tmp/pic2-resize.png', img.format)

#Relative Path
#Image on which we want to paste
img = Image.open("res/template/birthday.jpg")

#Relative Path
#Image which we want to paste
img2 = Image.open(".tmp/pic2-resize.png")
img.paste(img2, (1988, 60))

#Saved in the same relative location
img.save(".tmp/pic2-resize.png")

img = Image.open(".tmp/pic2-resize.png")
dw=ImageDraw.Draw(img)
x, y = 400, 1282
a, b = 700, 1140
myfnt=ImageFont.truetype('res/font/KaushanScript-Regular.ttf', 260)
mydfnt=ImageFont.truetype('res/font/Raphtalia Personal Use.ttf', 140)
# dw.text((x-1, y-1), "Ashwin", font=myfnt, fill="black")
# dw.text((x+1, y-1), "Ashwin", font=myfnt, fill="black")
# dw.text((x-1, y+1), "Ashwin", font=myfnt, fill="black")
# dw.text((x+1, y+1), "Ashwin", font=myfnt, fill="black")
dw.text((x, y), bname, font=myfnt, fill=(255, 255, 255), stroke_width=20, stroke_fill='black' )
dw.text((a, b), bdate, font=mydfnt, fill=(255, 255, 255), stroke_width=10, stroke_fill='black' )
img.save(f"output/{bname}.jpg")
##An additional argument for an optional image mask image is also available.
