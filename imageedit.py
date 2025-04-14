from PIL import Image
import os
from move import move

def startedit():
    def editor(xcoor, xcoor2, ycoor, urlist, name, xboard):
        cropimg = img.crop((xcoor, ycoor, xcoor2, ycoor+900))
        cropimg1 = img.crop((585, ycoor, 985, ycoor+900))
        cropimg3 = img.crop((xboard, 400, xboard + 700, 500))
        new_image = Image.new('RGB',(2*cropimg.size[0], 1050), (250,250,250))
        new_image.paste(cropimg3,(0, 0))
        new_image.paste(cropimg1,(0,80))
        new_image.paste(cropimg,(cropimg1.size[0],80))
        new_image.save(f"{name[:-4]}{urlist}.jpg", "JPEG")
        move("image", f"{name[:-4]}{urlist}.jpg")
    def classfull(dayboard):
            editor(980, 1340, 1800, "7А", path, dayboard), editor(1340, 1710, 1800, "7Б", path, dayboard)
            editor(1710, 2045, 1800, "7В", path, dayboard), editor(2045, 2415, 1800, "6А", path, dayboard)
            editor(2415, 2755, 1800, "6Б", path, dayboard), editor(2755, 3120, 1800, "6В", path, dayboard)
            editor(3120, 3485, 1800, "5А", path, dayboard), editor(3485, 3840, 1800, "5Б", path, dayboard)
            editor(980, 1340, 475, "11А", path, dayboard), editor(1340, 1710, 475, "11Б", path, dayboard)
            editor(1710, 2045, 475, "10А", path, dayboard), editor(2045, 2415, 475, "10Б", path, dayboard)
            editor(2415, 2755, 475, "9А", path, dayboard), editor(2755, 3120, 475, "9Б", path, dayboard)
            editor(3120, 3485, 475, "8А", path, dayboard), editor(3485, 3840, 475, "8Б", path, dayboard)
    for path in os.listdir("image"):
        filename = fr"image\{path}"
        with Image.open(filename) as img:
            img.load()
            if filename == "image\Четверг.jpg": classfull(2040)
            if filename == "image\Суббота.jpg": classfull(2040)

startedit()