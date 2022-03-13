from time import sleep
from pynput.keyboard import Key, Controller
sleep(300)
keyboard = Controller()
while True:
    sleep(102)
    keyboard.press("#")
    keyboard.release("#")

    keyboard.press("!")
    keyboard.release("!")

    keyboard.press("m")
    keyboard.release("m")

    keyboard.press("i")
    keyboard.release("i")

    keyboard.press("n")
    keyboard.release("n")

    keyboard.press("e")
    keyboard.release("e")

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    sleep(102)

    keyboard.press("#")
    keyboard.release("#")

    keyboard.press("!")
    keyboard.release("!")

    keyboard.press("c")
    keyboard.release("c")

    keyboard.press("h")
    keyboard.release("h")

    keyboard.press("o")
    keyboard.release("o")

    keyboard.press("p")
    keyboard.release("p")

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    sleep(102)

    keyboard.press("#")
    keyboard.release("#")

    keyboard.press("!")
    keyboard.release("!")

    keyboard.press("f")
    keyboard.release("f")

    keyboard.press("o")
    keyboard.release("o")

    keyboard.press("r")
    keyboard.release("r")

    keyboard.press("a")
    keyboard.release("a")

    keyboard.press("g")
    keyboard.release("g")

    keyboard.press("e")
    keyboard.release("e")

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)