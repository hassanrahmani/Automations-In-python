import pyautogui
import time
print('goto desktop')
time.sleep(5)
#chrome
pyautogui.moveTo(36,111)
pyautogui.doubleClick()
time.sleep(10)
#goto the studio
pyautogui.write('https://studio.youtube.com/', interval=0.2)
pyautogui.press('enter')
time.sleep(5)
#click create button
pyautogui.moveTo(1474,99)
pyautogui.click()
#uplaod video
pyautogui.moveTo(1495,145)
pyautogui.click()
#select file
pyautogui.moveTo(805,580)
pyautogui.click()
time.sleep(2)
#locate the folder where video are saved
pyautogui.click(95,142)
time.sleep(1)
#select all videos in folder and uplaod them to youtube
pyautogui.hotkey('ctrl','a')
time.sleep(2)
pyautogui.click(1139,786)
