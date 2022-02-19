import numpy as np

from WINIGST.Models.Model import Model


class Simulation(object):
    def __init__(self, path: str):
        """
        :param path: The file path of the simulation
        """
        self.path = path
        with open(path, "rb") as f:
            self.text = f.read().decode('cp1252')
        self.headerText = self.text[:self.text.find("MODEL")]

        self.footerText = self.text[self.text.rfind("END_MODEL") + len("END_MODEL"):]
        self.middleText = self.text[len(self.headerText):-len(self.footerText)]

        lines = self.middleText.split("\n")
        modelEndings = [i for i in range(len(lines)) if lines[i] == "END_MODEL\r"]

        lineLengths = [len(lines[i]) for i in range(len(lines))]
        indicies = [0] + list(np.cumsum(lineLengths)[modelEndings]) + [len(self.middleText)]
        self.models = []
        for i in range(1, len(indicies) - 1):
            modelText = self.middleText[
                        self.middleText.rfind("MODEL", indicies[i - 1], indicies[i]): indicies[i] + len(
                            "END_MODEL") + 1]
            if len(modelText) > 0:
                modelText = self.middleText[
                            self.middleText.rfind("MODEL ", 0, indicies[i]):self.middleText.find("END_MODEL",
                                                                                                 indicies[i]) + len(
                                "END_MODEL")]
                self.models.append(Model(modelText))

    def __str__(self):
        # mid = self.middleText
        # for model in self.models:
        #     mid = mid.replace(model.originalText, model.text)
        return self.headerText + self.middleText + self.footerText

    def update(self):
        for model in self.models:
            if model.originalText != model.text:
                self.middleText = self.middleText.replace(model.originalText, model.text)
                model.originalText = model.text

    def saveAs(self, fileName: str):
        self.update()
        string = str(self)
        with open(fileName, "wb") as f:
            f.write(string.encode('cp1252'))


if __name__ == '__main__':
    sim = Simulation("SIMPLIFIED-VERSION.NMT")
    z = 3
