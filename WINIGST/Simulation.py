import numpy as np
from util import BigIntersection


class Model(object):
    def __init__(self, text: str):
        self.originalText = text
        self.text = text

    def __str__(self):
        return self.text

    def getAttribute(self, attribute: str):
        """
        :param attribute: The Name of the attribute is the first word in the line of the file that describes
         the attribute
        :return: None if the attribute is not in the model
                A list containing a sub list for each row of the model definition that has the attribute
                Each sublist is a list of values on that row of the attribute.
                e.g.
                If the model definition was
                 MODEL 110
                 DEV_TITLE Equivalent Source (3-Phase)
                 NUMERIC_ID 1
                 COORDINATES -577 -232 -580 -232
                 CIRCUITS 1
                 INTERFACES SOURCE
                 PARAMETERS 69.282 2 0.13225 1.3225 0.13225 1.3225 0.26450 3.9675
                 PARAMETERS 0 100.0 115.00 0.001 0.01 0.001 0.01 0.002
                 PARAMETERS 0.03 120.000 0 60.00 1500.0 120.0 84.0 0
                 PARAMETERS 0.1 0.5
                 END_MODEL
                Then getAttribute("PARAMETERS") would return
                [
                ['69.282', '2', '0.13225', '1.3225', '0.13225', '1.3225', '0.26450', '3.9675'],
                ['0', '100.0', '115.00', '0.001', '0.01', '0.001', '0.01', '0.002'],
                ['0.03', '120.000', '0', '60.00', '1500.0', '120.0', '84.0', '0'],
                ['0.1', '0.5']
                ]
        """
        if attribute not in self.attributes:
            return None
        return [line.split(" ")[1:] for line in self.text.split("\n") if attribute in line]

    def insertAttribute(self, index: int, name: str, values: list):
        """
        :param index: index in self.attributes to insert
        :param name: The name of the attribute
        :param values: List containing a sub lists for each row of the model definition that the attribute should be on
                    Each sublist is a list of values to assign to the attribute
        """
        lines = self.text.split("\n")
        beforeAttribute = lines[:index]
        afterAttribute = lines[index:]
        attributeLines = [name + " " + " ".join(subL) for subL in values]
        self.text = "\n".join(beforeAttribute) + "\n" + "\n".join(attributeLines) + "\n" + "\n".join(afterAttribute)

    def discardAttribute(self, name: str):
        attrs = self.attributes
        lines = self.text.split("\n")
        self.text = "\n".join([lines[i] for i in range(len(lines)) if attrs[i] == name])

    def setAtribute(self, name: str, values: list):
        """
        :param name: The name of an attribute that is already in the model
        :param values: List containing a sub lists for each row of the model definition that the attribute should be on
                    Each sublist is a list of values to assign to the attribute
        """
        index = self.attributes.index(name)
        self.discardAttribute(name)
        self.insertAttribute(index, name, values)

    @property
    def attributes(self):
        attrs = []
        for line in [x for x in self.text.split("\n") if len(x) > 0]:
            if " " not in line:
                attrs.append(line)
            else:
                attrs.append(line[:line.find(" ")])
        return attrs


class Simulation(object):
    def __init__(self, path: str):
        """
        :param path: The file path of the simulation
        """
        self.path = path
        with open(path, "r") as f:
            self.text = f.read()
        self.headerText = self.text[:self.text.find("MODEL")]

        self.footerText = self.text[self.text.rfind("END_MODEL") + len("END_MODEL"):]
        self.middleText = self.text[len(self.headerText):-len(self.footerText)]

        lines = self.middleText.split("\n")
        modelEndings = [i for i in range(len(lines)) if lines[i] == "END_MODEL"]

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
        mid = self.middleText
        for model in self.models:
            mid = mid.replace(model.originalText, model.text)
        return self.headerText + mid + self.footerText

    def saveAs(self, fileName: str):
        string = str(self)
        with open(fileName, "w") as f:
            f.write(string)


if __name__ == '__main__':
    sim = Simulation("SIMPLIFIED-VERSION.NMT")
    z = 3
