import PIL
from PIL import Image
#Open Image
img = Image.open('src.jpg')
pix = img.load()
#Print Size of Image
print(img.size)
#String of Pixels 
pixels = ""
#Fill the String with the pixels
for py in range(0,img.size[1]):
    for px in range(0,img.size[0]):
        pixels+=str(pix[px,py])
    pixels+="\n"
#Print the String
print(pixels)