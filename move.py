import shutil
import os

def move(dir, file1):
    shutil.copy(os.path.join('.', file1), os.path.join('%s' % dir))
    os.remove(os.path.join('.', file1))