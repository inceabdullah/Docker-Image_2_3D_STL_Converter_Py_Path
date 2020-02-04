from time import sleep
from pynputEasy import mClick, mDoubleClick, oneKey, tabKey, keyCombine, enterKey

sleepK = 1
sleepSec = 1

sleepTot = sleepK*sleepSec

def delayDesired():
    sleep(sleepTot)
    return True

def doIt():
    mClick(406, 514)
    delayDesired()
    keyCombine("alt+c")
    delayDesired()
    oneKey("t")
    delayDesired()
    tabKey(3)
    delayDesired()
    keyCombine("255")
    delayDesired()
    tabKey(7)
    delayDesired()
    enterKey()
    delayDesired()*3
    keyCombine("alt+i")
    delayDesired()
    oneKey("s")
    delayDesired()
    keyCombine("200")
    delayDesired()*3
    tabKey(12)
    delayDesired()
    enterKey()
    delayDesired()
    keyCombine("ctrl+shift+e")
    delayDesired()
    mDoubleClick(359, 420)
    delayDesired()*3
    keyCombine("alt+t")
    delayDesired()
    mClick(242, 720)
    delayDesired()
    keyCombine("png")
    delayDesired()
    enterKey()
    delayDesired()
    tabKey(3)
    delayDesired()
    enterKey()
    delayDesired()
    enterKey()
    delayDesired()
    mClick(406, 514)
    delayDesired()
    keyCombine("ctrl+q")
    delayDesired()
    tabKey(1)
    delayDesired()
    enterKey()


    return True


