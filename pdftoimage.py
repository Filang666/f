import os
from pdf2image import convert_from_path


for i in os.listdir('pdf'):
    pages = convert_from_path('./pdf/%s' % i, 500)
    print(i)
    for count, page in enumerate(pages):
        page.save(f'out{count}.jpg', 'JPEG')