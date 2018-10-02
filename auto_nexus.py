# import necessary libraries
import win32
import win32api
import win32con
import winsound
from PIL import ImageGrab
import time

VK_CODE = {'r': 0x52}


def screen_grab():
    im = ImageGrab.grab()
    return im


# get and store coordinates of health bar at 35% in function
def get_cords():
    x, y = win32api.GetCursorPos()
    print(x, y)


# bar_color RGB = 84,84,84
# health_bar RGB = 224,52,52
class Health:
    low = (949, 353)
    med = (982, 353)
    high = (1028, 350)
    screen_change = (122, 435)
    bar_color = (1031, 329)


# function for when health bar reaches threshold, R key is automatically pressed
# on keyboard
# MUST USE THIS IN CONSOLE while True:
def main():
    s = screen_grab()
    if s.getpixel(Health.med) == (84,84,84):
        win32api.keybd_event(VK_CODE['r'], 0, 0, 0)
        time.sleep(.01)
        win32api.keybd_event(VK_CODE['r'], 0, win32con.KEYEVENTF_KEYUP, 0)
    else:
        pass

while __name__ == "__main__":
    main()
