import pyautogui
import threading
from pynput.keyboard import Key, Listener

key_to_press = None
first_delay = 10

def on_press(key):
    global key_to_press
    
    if isinstance(key, Key):
        key_to_press = str(key).replace('Key.', '')
    else:
        key_to_press = key.char
    
    return False

print("Нажмите клавишу, которую нужно нажимать:")  

with Listener(on_press=on_press) as listener:
    listener.join()
    
if key_to_press is None:
    print("Клавиша не нажата")
else:
    delay = float(input("Введите интервал нажатия клавиши (сек): "))

    print("У тебя есть 10 секунд чтобы зайти в GTA 5")
    time.sleep(first_delay)

    while True:
        pyautogui.press(key_to_press)
        print(f"Нажата клавиша {key_to_press}")
        threading.Event().wait(delay)