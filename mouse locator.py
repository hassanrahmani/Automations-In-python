import pyautogui
import time

while True:
    wow = currentMouseX, currentMouseY = pyautogui.position()
    time.sleep(1)
    print(wow)