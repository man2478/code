import pyautogui
import time
while True:
    #get the position of the cuser
    x, y = pyautogui.position()
    #decide the pixcle around any object
    z = pyautogui.pixel(x, y)
    l = pyautogui.pixel(x-1, y)
    print(f"{z},{l}")
    time.sleep(1)
    if z[0] & z[1] & z[2] & l[0] & l[1] & l[2]!=255:# tu detect white pixcle

        pyautogui.press("space")
        time.sleep(.009)
    else:
        pass

