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

print("Press the key you want to press:")  

with Listener(on_press=on_press) as listener:
    listener.join()
    
if key_to_press is None:
    print("Key not pressed")
else:
    delay = float(input("Enter the key press interval (sec): "))

    print("You have 10 seconds to get into the right window.")
    threading.Event().wait(first_delay)

    while True:
        pyautogui.press(key_to_press)
        print(f"Нажата клавиша {key_to_press}")
        threading.Event().wait(delay)
