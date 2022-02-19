from WINIGST.Models.Model import Model
class RegulatingTransformer(Model):
    @property
    def Tap_Setting(self):
        params = self.getAttribute('PARAMETERS')
        return params[0][5]
    @Tap_Setting.setter
    def Tap_Setting(self, value):
        params = self.getAttribute('PARAMETERS')
        params[0][5] = value
        self.setAtribute('PARAMETERS', params)


if __name__ == '__main__':
    # Demo
    from WINIGST.Simulation import Simulation
    sim = Simulation('../New Sim.nmt')
    reg1Index = [i for i in range(len(sim.models)) if sim.models[i].NUMERIC_ID == '181'][0]
    sim.models[reg1Index] = RegulatingTransformer(sim.models[reg1Index])
    regulator1 = [x for x in sim.models if 'Regulating Transformer 1' in x.DEV_TITLE][0]
    tap = regulator1.Tap_Setting
    regulator1.Tap_Setting = '0.99'
    n = regulator1.NUMERIC_ID
    sim.update()
    sim.saveAs('Edited New Sim.NMT')

