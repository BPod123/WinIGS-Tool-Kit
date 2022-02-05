import pyautogui



from util import rectangleCenter, fineWindowsWithSubstringInName
from util.mouseActions import *
import win32gui
import numpy as np
from Window import Window
from enum import Enum
class MainScreenStates(Enum):
    NEW = 0
    OPENDED_FILE = 1

class WinIGS_T(Window):
    def __init__(self):
        super().__init__('AGC - WinIGS-T')
        self.state = MainScreenStates.NEW
    def newWindow(self):
        self.hwnd = fineWindowsWithSubstringInName("WinIGS-T")[0]



    @property
    def RunButton(self):
        """
        :return: The location of the Run button
        """
        return rectangleCenter(win32gui.GetWindowRect(self.children['Run'][0]))

    @property
    def PauseButton(self):
        """

        :return: The location of the Pause button
        """
        return rectangleCenter(win32gui.GetWindowRect(self.children['Pause'][0]))

    @property
    def StopButton(self):
        """

        :return: The location of the Stop button
        """
        return rectangleCenter(win32gui.GetWindowRect(self.children['Stop'][0]))

    @property
    def TDS_PARButton(self):
        """
        :return: The location of the TDS_PAR button (The button to the right of Stop)
        """
        return rectangleCenter(win32gui.GetWindowRect(self.children['TDS_PAR'][0]))

    @property
    def TDS_PHA_DISPButton(self):
        """
        :return: The location of the TDS_PHA_DISP button (The button two to the right of Stop)
        """
        return rectangleCenter(win32gui.GetWindowRect(self.children['TDS_PAR'][0]))

    @property
    def DieButton(self):
        """
        :return: The location of the button the die button (the button three to the right of Stop)
        """
        return rectangleCenter(win32gui.GetWindowRect(self.children['TDS_MCARLO'][0]))

    @property
    def TurtleButton(self):
        """
        :return: The location of the Turtle button
        """
        hwnds = self.children['Button1']
        rects = {hwnd: win32gui.GetWindowRect(hwnd) for hwnd in hwnds}  # leftX, topY, rightX, bottomY
        hwndPos = {hwnd: rectangleCenter(rects[hwnd]) for hwnd in hwnds}
        # The turtle is the left one
        hwnds.sort(key=lambda hwnd: hwndPos[hwnd][0])
        location = hwndPos[hwnds[0]]
        return hwndPos[hwnds[0]]

    @property
    def RabbitButton(self):
        """
        :return: The location of the Rabbit button
        """
        hwnds = self.children['Button1']
        rects = {hwnd: win32gui.GetWindowRect(hwnd) for hwnd in hwnds}  # leftX, topY, rightX, bottomY
        hwndPos = {hwnd: rectangleCenter(rects[hwnd]) for hwnd in hwnds}
        # The rabbit is the right one
        hwnds.sort(key=lambda hwnd: hwndPos[hwnd][0])
        return hwndPos[hwnds[1]]

    @property
    def setupZone(self):
        """
        :return: The HWND for the subwindow containing the buttons for create file, open file, the question mark button,
        and 'edit program options'
        """
        children = self.children['']
        children.sort(key=lambda hwnd: rectangleCenter(win32gui.GetWindowRect(hwnd)))
        zone = children[0]
        return zone

    @property
    def CreateNewStudyButton(self):
        """
        :return: The location of the 'Create a new WinIGS Study Case...' button
        """
        setup = self.setupZone
        # There are 4 buttons aligned vertically, we are looking for the top button location
        leftX, topY, rightX, bottomY = win32gui.GetWindowRect(setup)
        buttonHeight = (bottomY - topY) // 4
        buttonCenterX = leftX + (rightX - leftX) // 2
        return buttonCenterX, topY + buttonHeight // 2

    @property
    def OpenStudyButton(self):
        """
        :return: The location of the  'Open WinIGS Study Case' button
        """
        setup = self.setupZone
        # There are 4 buttons aligned vertically, we are looking for the top button location
        leftX, topY, rightX, bottomY = win32gui.GetWindowRect(setup)
        buttonHeight = (bottomY - topY) // 4
        buttonCenterX = leftX + (rightX - leftX) // 2
        return buttonCenterX, topY + 3 * buttonHeight // 2

    @property
    def AboutIGSButton(self):
        """
        :return: The location of the 'Program Information' button
        """
        setup = self.setupZone
        # There are 4 buttons aligned vertically, we are looking for the top button location
        leftX, topY, rightX, bottomY = win32gui.GetWindowRect(setup)
        buttonHeight = (bottomY - topY) // 4
        buttonCenterX = leftX + (rightX - leftX) // 2
        return buttonCenterX, topY + 5 * buttonHeight // 2

    @property
    def OptionsButton(self):
        """
        :return: The location of the 'Select Options...' button
        """
        setup = self.setupZone
        # There are 4 buttons aligned vertically, we are looking for the top button location
        leftX, topY, rightX, bottomY = win32gui.GetWindowRect(setup)
        buttonHeight = (bottomY - topY) // 4
        buttonCenterX = leftX + (rightX - leftX) // 2
        return buttonCenterX, topY + 7 * buttonHeight // 2
    @property
    def XOutCurrentFileButton(self):
        z = 3
        # Click the x
        xPercentFromRight = 0.0125
        yPercentFromTop = 0.0541018
        x = round(self.rect[2] - (self.rect[2] - self.rect[0]) * xPercentFromRight)
        y = round(self.rect[1] + (self.rect[3] - self.rect[1]) * yPercentFromTop)
        # 1526, 145
        return (x, y)



