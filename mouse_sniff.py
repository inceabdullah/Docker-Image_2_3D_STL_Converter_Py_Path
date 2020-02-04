from pynput.mouse import Button, Controller
from time import sleep

mouse = Controller()
def mPosition():
    return mouse.position

while True:
    print(mPosition())
    sleep(1)