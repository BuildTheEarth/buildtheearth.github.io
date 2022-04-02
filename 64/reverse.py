from PIL import Image
import json

colors = {'white': (255, 255, 255, 255),
'lightgray': (228, 228, 228, 255),
'darkgray': (136, 136, 136, 255),
'black': (34, 34, 34, 255),
'lightpink': (255, 167, 209, 255),
'red': (229, 0, 0, 255),
'orange': (229, 149, 0, 255),
'brown': (160, 106, 66, 255),
'yellow': (229, 217, 0, 255),
'lightgreen': (148, 224, 68, 255),
'green': (2, 190, 1, 255),
'cyan': (0, 211, 221, 255),
'grayblue': (0, 131, 199, 255),
'blue': (0, 0, 234, 255),
'pink': (207, 110, 228, 255),
'purple': (130, 0, 128, 255),}

# open method used to open different extension image file
im = Image.new("RGBA", (1000,1000))
  
# This method will show image in any image viewer 
pixels = im.load()

with open("out.json") as f:
    final = json.load(f)

startX = 0
startY = 0

for i in range(1000):
    for j in range(1000):
        try:
            pixels[i, j] = colors[final[str((i + startX, j + startY))]]
        except:
            pixels[i, j] = (255,0,255, 255)
        

im.show()
im.save("pos.png")