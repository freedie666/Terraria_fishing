from PIL import ImageGrab
from PIL import Image
import time
import beepy


time.sleep(5)
snapshot = ImageGrab.grab()
save_path = "images-screenshots/screen.jpg"
snapshot.save(save_path)

beepy.beep(sound=1)
exit(1)