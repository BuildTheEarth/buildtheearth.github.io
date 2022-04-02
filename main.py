from PIL import Image
import json

colors = {(255, 255, 255): 'white',
(228, 228, 228): 'lightgray',
(190, 190, 190): 'lightgray',
(136, 136, 136): 'darkgray',
(34, 34, 34): 'black',
(0, 0, 0): 'black',
(255, 167, 209): 'lightpink',
(229, 0, 0): 'red',
(229, 149, 0): 'orange',
(160, 106, 66): 'brown',
(229, 217, 0): 'yellow',
(148, 224, 68): 'lightgreen',
(2, 190, 1): 'green',
(0, 211, 221): 'cyan',
(0, 131, 199): 'grayblue',
(0, 0, 234): 'blue',
(207, 110, 228): 'pink',
(130, 0, 128): 'purple',}

# open method used to open different extension image file
im = Image.open("img6.png").convert("RGBA")
  
# This method will show image in any image viewer 
pixels = im.load()

final = {}

startX = 298
startY = 476

for i in range(32):
    for j in range(32):
        try:
            if pixels[i, j][3] != 0: final[str((i + startX, j + startY))] = str(colors[(pixels[i, j][0], pixels[i, j][1], pixels[i, j][2])])
        except:
            if pixels[i, j][3] != 0:
                print(pixels[i, j])
        
with open("out.json", "w") as f:
    json.dump(final, f)
