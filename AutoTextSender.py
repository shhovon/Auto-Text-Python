import pyautogui
import time

comments= ["erjinrih" , "unv" , "wuneufn" , "rirfn"]

time.sleep(5)

for i in range(100):
    pyautogui.typewrite(comments[i%4])
    pyautogui.typewrite("\n")
    time.sleep(2)
