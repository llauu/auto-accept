from time import sleep
import pyautogui;

def click(x, y):
  pyautogui.click(x, y)

def check_screen():
  sleep(1)
  button = pyautogui.locateOnScreen('accept.png')

  if button != None:
    click(button.left, button.top)
    return True

  print('waiting...')
  return False

while True:
  if check_screen():
    print('match accepted')
    sleep(5)
    break


