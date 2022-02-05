from Window import Window
from util import rectangleCenter, hwndCenter as hwndCenter, pointDist, topWindow, leftWindow, rightWindow,bottomWindow
from win32gui import GetWindowRect

class UtilityPV(Window):
    @property
    def LineToNeutralInput(self):
        # Second highest child input
        possible = list(self.children[""])
        possible.sort(key = lambda x: (hwndCenter(x)[1], hwndCenter(x)[0]))
        return possible[1]
    @property
    def LineToLineInput(self):
        return min([x for x in self.children[""] if x != self.LineToNeutralInput], key = lambda hwnd: pointDist(hwndCenter(hwnd), hwndCenter(self.LineToNeutralInput)))

    @property
    def PhaseAngleInput(self):
        return min([x for x in self.children[""] if x != self.LineToNeutralInput and x != self.LineToLineInput],
                   key=lambda hwnd: pointDist(hwndCenter(hwnd), hwndCenter(self.LineToLineInput)))
    # def setResistanceOhms(self, resistances):
    #     """
    #
    #     :param resistances: Array of values for each input. Use None if you don't want to edit a value
    #     :return:
    #     """
    #     z  = 3