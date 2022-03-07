from PIL import Image,ImageGrab,ImageChops,ImageStat
import beepy
import time
import keyboard
import pyautogui

saving_images = False

# folder needs to be created
save_path = "images-screenshots/"

# how big of area should be cropped from a screen
area = 250

# rgb of fishing line
red = 249
green = 86
blue = 56


# RGB range for fishing line  - RGB +- RGB_range
RGB_range = 10

# treshold for detecting fish / detecting fishing line movement
fish_treshhold = 0.30

# num of cycles to perform in for loop
num_of_cycles = 100


# spravi screen obrazovky a vrati cropped
def get_screenshot():
    """
    Makes screenshot and croppes it
    """
    img = ImageGrab.grab()  # make screen

    width, height = img.size   # Get dimensions
    left = width/2 - area
    top = height/2 - area
    right = width/2 + area
    bottom = height/2 + area

    img = img.crop((left, top, right, bottom))
    return img

def is_pixel_in_range(pixel):
    """
    Checks if given pixel has desired RGB value and of it is in desired range
    """
    if red - RGB_range < pixel[0] < red + RGB_range:
        if green - RGB_range < pixel[1] < green + RGB_range:
            if blue - RGB_range < pixel[2] < blue + RGB_range:
                return True
    return False


def to_black_n_white(img):
    """
    Transforms image to black and white where white is fishing line color, others are black
    """
    pixels = img.load()
    for i in range(img.size[0]): # for every pixel:
        for j in range(img.size[1]):
            if is_pixel_in_range(pixels[i,j]):
                pixels[i,j] = (255,255,255)
            else:
                pixels[i,j] = (0,0,0)

    return img


def image_comparison(img1,img2):
    """
    Finds differences between images and returns mean color of result image
    """

    diff = ImageChops.difference(img1, img2)
    stat = ImageStat.Stat(diff)
    return stat.mean[0]




if __name__ == '__main__':

    first_loop = True
    time.sleep(5)

    for screen_num in range(num_of_cycles): #10000

        # keyboard input in case mouse is bugged
        if keyboard.is_pressed('q'):
            print('Exiting')
            beepy.beep(sound=1)
            break  # finishing the loop


        img = get_screenshot()
        img = to_black_n_white(img)

        if first_loop:
            previous_img = img
            first_loop = False
            continue

        diff_coef = image_comparison(previous_img,img)
        print(diff_coef)

        # fish detected
        if diff_coef >= fish_treshhold:
            #print("fish " +str(screen_num))

            # catch fish
            pyautogui.mouseDown(button='left')
            pyautogui.mouseUp(button='left')
            time.sleep(1)

            # throw fishing line
            pyautogui.mouseDown(button='left')
            pyautogui.mouseUp(button='left')
            time.sleep(1.5)
            first_loop = True

        previous_img = img

        if saving_images:
            path = save_path + "screen" + str(screen_num) + ".jpg"
            img.save(path)
        time.sleep(0.1)

    # make beep sound at the end
    beepy.beep(sound=1)

