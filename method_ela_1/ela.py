#importing libs


from PIL import ImageChops
import PIL.Image
import os

# feature engineering - Error Level Analysis
def ELA(img_path):
        DIR = "temp/"
        TEMP = "temp.jpg"
        SCALE = 10
        original = PIL.Image.open(img_path)
        if(os.path.isdir(DIR) == False):
                os.mkdir(DIR)
        original.save(TEMP, quality=90)
        temporary = PIL.Image.open(TEMP)
        diff = ImageChops.difference(original, temporary)
        d = diff.load()
        WIDTH, HEIGHT = diff.size
        for x in range(WIDTH):
                for y in range(HEIGHT):
                        d[x, y] = tuple(k * SCALE for k in d[x, y])

        diff.save(DIR+"ela_img.jpg")