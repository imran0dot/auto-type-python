import pyautogui as pg
import time

message = input("Enter the message: ")
range_value = int(input("Enter the range: "))

time.sleep(5)
for x in range(range_value):
    pg.typewrite(message)
    pg.press('enter')