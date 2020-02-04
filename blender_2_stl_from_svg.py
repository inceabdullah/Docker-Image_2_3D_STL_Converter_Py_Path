from time import sleep
from pynputEasy import mClick, mRClick, mDoubleClick, oneKey, tabKey, keyCombine, enterKey

sleepK = 3
sleepSec = 1

sleepTot = sleepK*sleepSec

def delayDesired():
    sleep(sleepTot)
    return True

def doIt():

    mClick(520, 320)
    delayDesired()
    oneKey("a")
    delayDesired()
    oneKey("x")
    delayDesired()
    enterKey()
    delayDesired()

    mClick(40,40)
    delayDesired()
    oneKey("i")
    delayDesired()

    oneKey("s")
    delayDesired()
    mClick(76, 177)
    delayDesired()
    mDoubleClick(360, 225)
    delayDesired()
    mDoubleClick(360, 205)
    delayDesired()
    mDoubleClick(360, 205)
    delayDesired()
    mDoubleClick(360, 205)
    delayDesired()
    mClick(960, 155)
    delayDesired()
    mClick(270, 95)
    delayDesired()
    mClick(270, 135) #oneKey("s")
    delayDesired()
    mClick(470,135) #oneKey("g")
    delayDesired()
    mClick(270, 95)
    delayDesired()
    oneKey("v")
    delayDesired()
    oneKey("m")
    delayDesired()
    tabKey()
    delayDesired()
    oneKey("a")
    delayDesired()
    oneKey("e")
    delayDesired()
    oneKey("z")
    delayDesired()
    keyCombine("0.005")
    delayDesired()
    enterKey()
    delayDesired()
    mClick(40, 40)
    delayDesired()
    oneKey("e")
    delayDesired()
    oneKey("t")
    delayDesired()
    mClick(85, 180)
    delayDesired()

    mDoubleClick(340, 225)
    delayDesired()
    mDoubleClick(340, 205)
    delayDesired()
    mDoubleClick(340, 205)
    delayDesired()
    enterKey()
    delayDesired()

    mClick(40, 40)
    delayDesired()

    oneKey("q")
    delayDesired()

    oneKey("d")

    



    return True


