from WINIGST.Models.Model import Model
class Capacitor(Model):
    @property
    def isClosed(self):
        params = self.getAttribute('PARAMETERS')
        return params[0][0] == '1'
    @isClosed.setter
    def isClosed(self, value:bool):
        params = self.getAttribute('PARAMETERS')
        params[0][0] = '1' if value else '0'
        self.setAtribute('PARAMETERS', params)
if __name__ == '__main__':
    # Demo
    from WINIGST.Simulation import Simulation
    sim = Simulation('../New Sim.nmt')
    cap1Index = [i for i in range(len(sim.models)) if sim.models[i].NUMERIC_ID == '26'][0]
    sim.models[cap1Index] = Capacitor(sim.models[cap1Index])
    capacitor1 = sim.models[cap1Index]
    isClosed = capacitor1.isClosed
    capacitor1.isClosed = False
    sim.update()
    sim.saveAs('Edited New Sim.NMT')
    z = 3

    z = 3