from WINIGST.Models.Model import Model


class UtilityPV(Model):
    @property
    def PhaseAngle(self):
        params = self.getAttribute('PARAMETERS')
        return params[0][1]


    @PhaseAngle.setter
    def PhaseAngle(self, value):
        params = self.getAttribute('PARAMETERS')
        params[0][1] = value
        self.setAtribute('PARAMETERS', params)


if __name__ == '__main__':
    from WINIGST.Simulation import Simulation

    sim = Simulation('../New Sim.nmt')
    index = [i for i in range(len(sim.models)) if sim.models[i].NUMERIC_ID == '69'][0]
    sim.models[index] = UtilityPV(sim.models[index])
    pv = sim.models[index]
    phaseAngle = pv.PhaseAngle
    pv.PhaseAngle = '65'

    sim.saveAs('Edited New Sim.NMT')
    z = 3
