import os
if os.name == "nt":
    import msvcrt
elif os.name == "posix":
    from pynput import keyboard
else:
    exit(127)

keys = set()


def posix_onpress(key):
    keys.add(key)

def posix_onrelease(key):
    try:
        keys.remove(key)
    except KeyError:
        pass

def get_keypress():
    if os.name == "nt":
        while True:
            if msvcrt.kbhit():
                print(msvcrt.getch())
    elif os.name == "posix":
        with keyboard.Listener(on_press=posix_onpress, on_release=posix_onrelease):
            while True:
                for key in keys:
                    print(key.char)

from key_getter import KeyGetter
import time

def test1():
    print("test1")
    k = KeyGetter()
    try:
        while True:
            if k.kbhit():
                print(f"got: {repr(k.getchar(False))}")
            time.sleep(0.005)
    except KeyboardInterrupt:
        pass
if __name__ == "__main__":
    print(os.get_terminal_size())
    print(os.name)
    #get_keypress()
    test1()
