import pyautogui
import time

comments= ["some" , "random" , "repeating" , "texts"]

time.sleep(5)

for i in range(100):
    pyautogui.typewrite(comments[i%4])
    pyautogui.typewrite("\n")
    time.sleep(2)
