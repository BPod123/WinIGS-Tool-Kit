from WINIGST.MainScreen import WinIGS_T
from WINIGST.Menues.OpenStudyCaseScreen import OpenStudyCase
from time import sleep
import pyautogui
class Procedure(object):
    def __init__(self, winIGST=None):
        if winIGST is None:
            self.winigsT = WinIGS_T()
        else:
            self.winigsT = winIGST
    def openFile(self, fileNum):
        pyautogui.moveTo(*self.winigsT.OpenStudyButton)
        pyautogui.click()
        openWindow = OpenStudyCase()
        sleep(1)
        pyautogui.moveTo(*openWindow.positionOfFile(fileNum))
        sleep(1)
        pyautogui.doubleClick()
        sleep(1)


