from Window import Window
from util import rectangleCenter, hwndCenter as hwndCenter, pointDist
from win32gui import GetWindowRect
class RegulatingTransformer(Window):
    @property
    def AcceptButton(self):
        return rectangleCenter(GetWindowRect(self.children['Accept'][0]))

    @property
    def CancelButton(self):
        return hwndCenter(self.children['Cancel'][0])
    def DeltaButton(self, side:int):
        """
        :param side: 1 or 2
        :return: The position of the button
        """
        if side == 1:
            return min([hwndCenter(hwnd) for hwnd in self.children['Delta']],
                       key=lambda x: GetWindowRect(x)[0])
        if side == 2:
            return max([hwndCenter(hwnd) for hwnd in self.children['Delta']],
                       key=lambda x: GetWindowRect(x)[0])
    def WyeButton(self, side:int):
        """
            :param side: 1 or 2
            :return: The position of the button
        """
        if side == 1:
            return min([hwndCenter(hwnd) for hwnd in self.children['Wye']],
                       key=lambda x: GetWindowRect(x)[0])
        if side == 2:
            return max([hwndCenter(hwnd) for hwnd in self.children['Why']],
                       key=lambda x: GetWindowRect(x)[0])
    @property
    def StandardButton(self):
        return hwndCenter(self.children['Standard'][0])

    @property
    def AlternateButton(self):
        return hwndCenter(self.children['Alternate'][0])
    @property
    def TransformerRatingInput(self):
        return hwndCenter(min([x for x in self.children[""] if hwndCenter(x)[1] > self.AlternateButton[1]],
                                key=lambda hwnd: hwndCenter(hwnd)))
    @property
    def MaximumInput(self):
        return hwndCenter(min([x for x in self.children[""] if hwndCenter(x)[1] > self.AlternateButton[1]],
                              key=lambda hwnd: (hwndCenter(hwnd)[0], -hwndCenter(hwnd)[1])))
    @property
    def MinimumInput(self):
        positions = [hwndCenter(x) for x in self.children[""]]
        return min((x for x in positions if x != self.MaximumInput), key = lambda x: pointDist(x, self.MaximumInput))
    @property
    def NumberOfTapsInput(self):
        positions = [hwndCenter(x) for x in self.children[""]]
        return min((x for x in positions if x not in (self.MaximumInput, self.MinimumInput)), key=lambda x: pointDist(x, self.MaximumInput))

