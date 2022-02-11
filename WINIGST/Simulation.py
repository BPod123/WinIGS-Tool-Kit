import numpy as np
class Model(object):
    def __init__(self, text:str):
        self.text = text
    def __str__(self):
        return self.text
class Simulation(object):
    def __init__(self, path:str):
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

        idLines = [i for i in range(len(lines)) if "NUMERIC_ID" in lines[i]]
        

        z = 3





if __name__ == '__main__':
    sim = Simulation("SIMPLIFIED-VERSION.NMT")
    z = 3
