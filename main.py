from PIL import Image,ImageGrab,ImageChops,ImageStat
import beepy
import time
import keyboard
import pyautogui


save_path = "images-screenshots/"

# rozmery vyrezu z obrazovky
area = 250

#rgb udice
red = 249
green = 86
blue = 56


# kolko +- RGB moze mat udica /  kolko sa detekuje
koef = 10

ryba_treshhold = 0.30

# skontroluje ci pixel ma pozadovanu rgb farbu +  keof buffer
def is_pixel_in_range(pixel):
    if red - koef < pixel[0] < red + koef:
        if green - koef < pixel[1] < green + koef:
            if blue - koef < pixel[2] < blue + koef:
                return True
    return False

# spravi screen obrazovky a vrati cropped
def get_screenshot():
    img = ImageGrab.grab()  # sprav screen


    #img = Image.open("images/Sample3.png")

    width, height = img.size   # Get dimensions
    left = width/2 - area
    top = height/2 - area
    right = width/2 + area
    bottom = height/2 + area
    img = img.crop((left, top, right, bottom))

    return img

# prehodi screen do ciernobielej, pricom biela bude farba udice a cierne bude zvysok
def to_black_n_white(img):
    pixels = img.load()
    for i in range(img.size[0]): # for every pixel:
        for j in range(img.size[1]):
            if is_pixel_in_range(pixels[i,j]):
                pixels[i,j] = (255,255,255)
            else:
                pixels[i,j] = (0,0,0)

    return img

#odcita obrazky od seba a vrati priemernu hodnotu farby pixelu na obrazku -> ak je cislo vacsie
def image_comparison(img1,img2):

    diff = ImageChops.difference(img1, img2)
    stat = ImageStat.Stat(diff)
    return stat.mean[0]




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    first_loop = True

    # zaciatok - zapnutie
    time.sleep(5)

    for screen_num in range(10000):
        if keyboard.is_pressed('q'):  # if key 'q' is pressed
            print('Exitujem')
            beepy.beep(sound=1)
            break  # finishing the loop


        img = get_screenshot()
        img = to_black_n_white(img)

        if first_loop:
            previous_img = img
            first_loop = False
        else:
            diff_coef = image_comparison(previous_img,img)
            print(diff_coef)

            # chytena ryba
            if diff_coef >= ryba_treshhold:
                print("fish")
                #chyt rybu
                pyautogui.mouseDown(button='left')
                pyautogui.mouseUp(button='left')
                time.sleep(1)

                #nahod udicu
                pyautogui.mouseDown(button='left')
                pyautogui.mouseUp(button='left')
                time.sleep(1.5)
                first_loop = True
            previous_img = img


        #path = save_path + "screen" + str(screen_num) + ".jpg"
        #img.save(path)
        time.sleep(0.1)

    beepy.beep(sound=1)
    #img.show()

