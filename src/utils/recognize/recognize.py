from utils.recognize.controllers import keyboard, mouse
from utils.recognize.clipboard import clipboard
from pynput.keyboard import Key
from pynput.mouse import Button
from time import sleep

def recognize() -> None:
    # Open photo:
    keyboard.tap(Key.cmd)
    sleep(1)
    keyboard.type('C:\\Users\\yaz008\\Desktop\\github\\rsolver\\temp.png')
    sleep(1)
    keyboard.tap(Key.enter)
    sleep(1)

    # Recognize text:
    keyboard.press(Key.cmd)
    keyboard.press(Key.shift)
    keyboard.press('a')
    keyboard.release('a')
    keyboard.release(Key.shift)
    keyboard.release(Key.cmd)
    sleep(1)
    mouse.position = (672, 34)
    mouse.click(Button.left)
    sleep(1)
    mouse.position = (653, 118)
    mouse.click(Button.left)
    sleep(1)
    mouse.position = (412, 255)
    mouse.press(Button.left)
    sleep(1)
    mouse.move(dx=642, dy=371)
    mouse.release(Button.left)
    sleep(1)

    # Close photo:
    mouse.position = (1450, 16)
    mouse.click(Button.left)

    # Return clipboard content:
    with clipboard() as clipboard_data:
        return clipboard_data