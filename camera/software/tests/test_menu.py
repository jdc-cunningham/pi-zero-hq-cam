from PIL import Image
from PIL import ImageChops

img_one = Image.open("C:/Users/Green/projects/pi-zero-hq-cam/camera/software/tests/boot.jpg")
img_two = Image.open("C:/Users/Green/projects/pi-zero-hq-cam/camera/software/tests/diff.png")

diff = ImageChops.difference(img_one, img_one)

def func():
    return diff.getbbox() == None

def test_answer():
    print(func())
    assert func() == True