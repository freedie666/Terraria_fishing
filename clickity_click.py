import pyautogui
import time
import beepy

time.sleep(4)
beepy.beep(sound=1)


#pyautogui.click(1000, 1000)
pyautogui.mouseDown(button='left')
pyautogui.mouseUp(button='left')





# import time
#
# import win32api,win32con
#
#
# def click():
#     x, y = win32api.GetCursorPos()
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
#
#
#
# time.sleep(3)
# click()
#





# import time
#
# from pynput.mouse import Button, Controller
#
# mouse = Controller()
#
# time.sleep(3)
# # Read pointer position
# print('The current pointer position is {0}'.format(
#     mouse.position))
#
# # # Set pointer position
# # mouse.position = (10, 20)
# # print('Now we have moved it to {0}'.format(
# #     mouse.position))
#
# # Move pointer relative to current position
# mouse.move(5, -5)
#
# # Press and release
# mouse.press(Button.left)
# mouse.release(Button.left)
#
# # Double click; this is different from pressing and releasing
# # twice on Mac OSX
# mouse.click(Button.left, 2)
#
# # Scroll two steps down
# mouse.scroll(0, 2)
