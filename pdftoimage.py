import os
from pdf2image import convert_from_path
from move import move
from shutil import rmtree


def converter():
    for i in os.listdir('pdf'):
        pages = convert_from_path('./pdf/%s' % i, 500)
        rmtree("image")
        os.mkdir("image")
        for count, page in enumerate(pages):
            page.save(f'{i[:-4]}.jpg', 'JPEG')
            move('image', f'{i[:-4]}.jpg')

