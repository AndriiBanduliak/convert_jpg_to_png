import os
from PIL import Image

DIRECTORY = "Test"
FROM_EXTENTION = ".jpg"
TO_EXTENTION = ".png"
MAX_SIZE = (1024, 1024)


def walk(directory):
    for root, dirs, files in os.walk(directory):
        for name in files:
            conversion(os.path.join(root, name))


def conversion(file):
    resize(file)
    name, extension = os.path.splitext(file)
    if extension == FROM_EXTENTION:
        im = Image.open(file)
        im.save(name+TO_EXTENTION)
        os.remove(file)

def resize(file):
    im = Image.open(file)
    im.thumbnail(MAX_SIZE, Image.ANTIALIAS)
    im.save(file)

if __name__ == "__main__":
    walk(DIRECTORY)
