from util import findWindowsByName
from enum import Enum
from Window import Window
import pyautogui
import win32gui
from util import rectangleCenter, rectanglesInsideAnother, moveAndWait, hwndCenter, pointDist, rectPoints
class StudyType(Enum):
    TIME_DOMAIN = 1
    FREQUENCY_DOMAIN_IGS = 2
    FREQUENCY_DOMAIN_PSA = 3
    PLAYBACK_DATA = 4


class OpenStudyCase(Window):
    def __init__(self):
        super().__init__('Open WinIGS Study Case')
    @property
    def chooseFileHwnd(self):
        return self.children['List1'][0]
    @property
    def fileListHeaderHwnd(self):
        """
        :return: The HWND for the rectangle at the top of the choose tile hwnd. The part that says:
        Case            Date/Time           Description
        """
        return Window(self.chooseFileHwnd).children[""][0]
    def positionOfFile(self, n:int):
        """
        :param n: The number of files from the top (0 is the top file in the list)
        :return: The x,y position of the file button.
        """
        fHeaderRect = win32gui.GetWindowRect(self.fileListHeaderHwnd)
        height = (fHeaderRect[3] - fHeaderRect[1])
        percentLeft = int(fHeaderRect[0] + 0.01 * (fHeaderRect[2] - fHeaderRect[0]))
        fileHeaderRectCenterY = fHeaderRect[1] + int(0.8 * (fHeaderRect[3] - fHeaderRect[1]))
        return (percentLeft, fileHeaderRectCenterY + height + int(height * n))


# 417 436 452 # 17.5 in between them
# x at 511
# Rectangle: (466, 373, 1234, 763)
# Top File at 511, 417 = (left + 0.058% width, top + 0.112% Height)
# Next File at (left + 0.058% width +
# Top file at Description position shifted down the height of Description

if __name__ == '__main__':
    from util import launchApplication
    from WINIGST.MainScreen import WinIGS_T
    from time import sleep
    import pyautogui
    launchApplication('WINIGS-T')
    sleep(1)
    winigsT = WinIGS_T()
    pyautogui.moveTo(*winigsT.OpenStudyButton)
    pyautogui.click()
    openWindow = OpenStudyCase()
    sleep(1)
    pyautogui.moveTo(*openWindow.positionOfFile(6))
    sleep(1)
    pyautogui.doubleClick()
    sleep(1)
    # locationPrecents = ((948 - winigsT.windowRect[0]) / (winigsT.windowRect[2] - winigsT.windowRect[0]),
    #  (548 - winigsT.windowRect[1]) / (winigsT.windowRect[3] - winigsT.windowRect[1]))
    locationPrecents = (0.6222222222222222, 0.6534914361001317)
    location =  (winigsT.rect[0] + locationPrecents[0] * (winigsT.rect[2] - winigsT.rect[0]), winigsT.rect[1] + locationPrecents[1] * (winigsT.rect[3] - winigsT.rect[1]))
    pyautogui.moveTo(*location)
    pyautogui.doubleClick()
    # Need to find the window that is not winigsT and it is covering location
    while(True):
        print(pyautogui.position())
        sleep(0.5)
    #999 603
    z = 3