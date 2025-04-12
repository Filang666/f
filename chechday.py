import numpy as np
from PIL import Image
import os
def fullcheck():
    def cheDay(cday):
        filename = fr"{cday}.jpg"
        with Image.open(filename) as cday1:
            cday1.load()
        cday_array = np.asarray(cday1)
        return cday_array
    def checkrename(day1):
        for path in os.listdir("image"):
            filename = fr".\image\{path}"
            with Image.open(filename) as day:
                day.load()
                cropday = day.crop((0, 0, 330, 90))
                day_array = np.asarray(cropday)
                if np.allclose(day_array, cheDay(f"{day1}"), atol=100):
                    if path[:2] == 10 or 11:
                        os.rename(filename, fr".\image\{day1}{path[:3]}.jpg")
                    else:
                        os.rename(filename, fr".\image\{day1}{path[:2]}.jpg")
    
    
    checkrename("Понедельник")
    checkrename("Вторник")
    checkrename("Среда")
    checkrename("Четверг")
    checkrename("Пятницы")
    checkrename("Суббота")