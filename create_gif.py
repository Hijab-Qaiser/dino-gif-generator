import imageio.v3 as iio
import os

folder = os.path.dirname(__file__)

filenames = ["dino1.png", "dino2.png", "dino3.png", "dino4.png"]
images = []

for filename in filenames:
    filepath = os.path.join(folder, filename)
    images.append(iio.imread(filepath))

iio.imwrite(os.path.join(folder, "dino.gif"), images, duration=500, loop=0)
