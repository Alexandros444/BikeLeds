import PIL
import array
from PIL import Image
img = Image.open('src.png')
pix = img.load()
print(img.size)
lines = "byte PH[]={\n  "
pixels = ""
for py in range(0,img.size[1]):
    for px in range(0,img.size[0]):
        pixels+=str(pix[px,py])
        if(pix[px,py][0] == 255):
            lines+="0"
        elif(pix[px,py][0] == 0):
            lines+="1"
        else:
            lines+="X"
        if((px != img.size[0]-1) | (py != img.size[1]-1)):
            lines+=","
        #else:
            #print(str(px)+" "+str(py)+" "+str(int(img.size[1]-1))+""+str(pix[py,py]))
    lines+="\n"
    pixels+="\n"
    if(py != img.size[1]-1):
        lines+="  "
lines += "};"
out = open("out.txt","wt")
print(lines)
print(pixels)
out.write(lines)
out.close()
img.close()