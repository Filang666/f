from PIL import Image
import os
for path in os.listdir("image"):
    filename = fr"image\{path}"
    with Image.open(filename) as img:
        img.load()
    cropimg = img.crop((500, 100, 300, 800))
    cropimg.show()