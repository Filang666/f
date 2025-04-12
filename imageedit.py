from PIL import Image
import os
from move import move

def startedit():
    listclass = ["7А", "7Б", "7В"]
    listclass1 = ["6А", "6Б", "6В", "5А", "5Б"]
    listclass3 = ["11А", "11Б", "10А"]
    listclass4 = [ "10Б", "9А", "9Б", "8А", "8Б"]
    def editor(xcoor, ycoor, urlist, name):
        for size1 in range(len(urlist)):
            cropimg = img.crop((xcoor + 370*size1, ycoor, xcoor + 370 + 370*size1, ycoor+900))
            cropimg1 = img.crop((590, 1800, 985, 2780))
            cropimg3 = img.crop((2040, 400, 2750, 470))
            new_image = Image.new('RGB',(2*cropimg.size[0], 1050), (250,250,250))
            new_image.paste(cropimg3,(0, 0))
            new_image.paste(cropimg1,(0,80))
            new_image.paste(cropimg,(cropimg1.size[0],80))
            new_image.save(f"{urlist[size1]}{name}.jpg", "JPEG")
            move("image", f"{urlist[size1]}{name}.jpg")
            size1 += 1
    for path in os.listdir("image"):
        filename = fr"image\{path}"
        with Image.open(filename) as img:
            img.load()
            print(len(listclass))
            editor(980, 1800, listclass, path)
            editor(2020, 1800, listclass1, path)
            editor(980, 470, listclass3, path)
            editor(2020, 470, listclass4, path)
