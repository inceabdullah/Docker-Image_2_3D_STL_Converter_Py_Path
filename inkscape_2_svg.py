from time import sleep
from pynputEasy import mClick, mRClick, mDoubleClick, oneKey, tabKey, keyCombine, enterKey, spaceKey, deleteKey, upKey

sleepK = 1
sleepSec = 1

sleepTot = sleepK*sleepSec

def delayDesired():
    sleep(sleepTot)
    return True

def doIt():
    mClick(500, 20)
    delayDesired()

    keyCombine("alt+f")
    delayDesired()
    oneKey("i")
    delayDesired()
    mClick(206, 214)
    delayDesired()
    mDoubleClick(430, 199)
    delayDesired()
    mDoubleClick(395, 178)
    delayDesired()
    mClick(395, 198)
    delayDesired()
    enterKey()
    delayDesired()

    enterKey()
    delayDesired()

    keyCombine("alt+p")
    delayDesired()

    oneKey("t")
    delayDesired()

    tabKey(3)
    delayDesired()

    keyCombine("0.065")
    delayDesired()

    tabKey(2)
    delayDesired()

    oneKey("2")
    delayDesired()

    tabKey(3)
    delayDesired()

    spaceKey()
    delayDesired()

    tabKey(1)
    delayDesired()

    spaceKey()
    delayDesired()

    tabKey(1)
    delayDesired()

    spaceKey()
    delayDesired()

    tabKey(5)
    delayDesired()

    enterKey()
    delayDesired()



    mRClick(49, 15)
    delayDesired()*2

    upKey()

    delayDesired()

    enterKey()

    #oneKey("c")
    delayDesired()

    mClick(160, 350)
    delayDesired()

    tabKey(1)
    delayDesired()

    deleteKey()
    delayDesired()

    mClick(160, 350)
    delayDesired()

    tabKey()
    delayDesired()

    keyCombine("alt+f")
    delayDesired()

    oneKey("a")
    delayDesired()

    mClick(190, 260)
    delayDesired()

    mDoubleClick(350, 240)
    delayDesired()

    mDoubleClick(350, 222)
    delayDesired()

    mDoubleClick(350, 222)
    delayDesired()

    enterKey()
    delayDesired()

    keyCombine("alt+f")
    delayDesired()

    oneKey("q")

    



    return True


