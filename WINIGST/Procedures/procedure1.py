from time import time

from util import launchApplication
from WINIGST.Menues import RegulatingTransformer
from WINIGST import WinIGS_T
from WINIGST.Menues import UtilityPV, RegulatingTransformer
from time import sleep
import pyautogui
from WINIGST  import OpenStudyCase
from Window import Window
from win32gui import GetWindowRect
import win32gui
from util import *
from util.mouseActions import *
class Procedure1(object):
    def __init__(self, winigst:WinIGS_T):
        """
        It is presumed that the file is opended in WinITGS-T at this point
        :param winigst:
        """
        self.winigsT = winigst
    @property
    def RegulatingTransformerButton(self):
        locationPrecents = (0.6222222222222222, 0.6534914361001317)
        location = (winigsT.rect[0] + locationPrecents[0] * (winigsT.rect[2] - winigsT.rect[0]),
                    winigsT.rect[1] + locationPrecents[1] * (winigsT.rect[3] - winigsT.rect[1]))
        return location
    @property
    def GeneratorButton(self):
        percents = (0.9048611111111111, 0.6455862977602108)
        return translationPoint(self.winigsT.rect, percents)


    def run(self):
        # # Open Regulating Transformer menu
        # locationPrecents = (0.6222222222222222, 0.6534914361001317)
        # location = (winigsT.windowRect[0] + locationPrecents[0] * (winigsT.windowRect[2] - winigsT.windowRect[0]),
        #             winigsT.windowRect[1] + locationPrecents[1] * (winigsT.windowRect[3] - winigsT.windowRect[1]))
        # currentWindows = allWindows()
        # pyautogui.moveTo(*location)
        # pyautogui.doubleClick()
        # sleep(1)
        # newWindows = [x for x in allWindows() if x not in currentWindows]
        # transformerMenu = RegulatingTransformer([x for x in newWindows if Window(x).parent == winigsT.hwnd][0])
        # enterInput(transformerMenu.TransformerRatingInput, "10.3")
        # enterInput(transformerMenu.MaximumInput, 5)
        # enterInput(transformerMenu.MinimumInput, 2)
        # clickPoint(transformerMenu.AcceptButton)


        doubleClickPoint(self.GeneratorButton)
        # Open Utility PV menu
        utilityMenu = UtilityPV(self.winigsT.doubleClickNewWindow(translationPoint(self.winigsT.rect, (0.5868055555555556, 0.9486166007905138))))
        enterInput(hwndCenter(utilityMenu.PhaseAngleInput), "70")
        clickPoint(hwndCenter(utilityMenu.children['Accept'][0]))
        # Go back to main screen
        clickPoint(winigsT.XOutCurrentFileButton)
        # Disconnect capacitor
        doubleRightClickPoint(translationPoint(self.winigsT.rect, (0.9618055555555556, 0.7233201581027668)))
        sleep(1)
        timeDomainParameters = self.winigsT.doubleClickNewWindow(self.winigsT.TDS_PARButton)
        clickPoint(hwndCenter(timeDomainParameters.children['Change File Path'][0]))
        pyautogui.write("Output {0}".format(time()))
        pyautogui.press('enter')
        clickPoint(hwndCenter(timeDomainParameters.children['OK'][0]))
        clickPoint(self.winigsT.RunButton)
        z =3

if __name__ == '__main__':
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
    winigsT.newWindow()
    procedure = Procedure1(winigsT)
    procedure.run()
    z = 3
    # locationPrecents = (0.6222222222222222, 0.6534914361001317)
    # location = (winigsT.windowRect[0] + locationPrecents[0] * (winigsT.windowRect[2] - winigsT.windowRect[0]),
    #             winigsT.windowRect[1] + locationPrecents[1] * (winigsT.windowRect[3] - winigsT.windowRect[1]))
    # winigsT.newWindow()
    # currentWindows = allWindows()
    # pyautogui.moveTo(*location)
    # pyautogui.doubleClick()
    # sleep(1)
    # newCurrentWindows = allWindows()
    # newWindows = [x for x in newCurrentWindows if x not in currentWindows]
    # hwnds = [hwnd for hwnd in windowsCoveringPoint(location) if hwnd != winigsT.hwnd]
    # newWindow = [Window(x) for x in newWindows if Window(x).parent == winigsT.hwnd][0]
    # # newWindow = Window([win32gui.GetParent(x) for x in newWindows if x in hwnds and rectangleCoveringPoint(win32gui.GetWindowRect(win32gui.GetParent(x)), location)][0])
    # z = 3
    # hwnd = max(hwnds, key = lambda x: (win32gui.GetWindowRect(x)[2] - win32gui.GetWindowRect(x)[0]) * (win32gui.GetWindowRect(x)[3] - win32gui.GetWindowRect(x)[1]))
    # w = Window(hwnd)
    # z = 3
