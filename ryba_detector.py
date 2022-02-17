from PIL import Image, ImageChops,ImageStat
import beepy


image1 = Image.open("images-screenshots/screen8.jpg")
image2 = Image.open("images-screenshots/screen9.jpg")

# image1 = Image.open("images-screenshots/screen0.jpg")
# image2 = Image.open("images-screenshots/screen5.jpg")


diff = ImageChops.difference(image1, image2)
stat = ImageStat.Stat(diff)
print(stat.mean)

diff.show()
















