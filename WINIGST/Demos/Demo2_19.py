from WINIGST.Simulation import Simulation
from WINIGST.Models import RegulatingTransformer, Capacitor, UtilityPV
if __name__ == '__main__':

    sim = Simulation('Sim.NMT')

    reg1Index = [i for i in range(len(sim.models)) if sim.models[i].NUMERIC_ID == '181'][0]
    sim.models[reg1Index] = RegulatingTransformer(sim.models[reg1Index])
    regulator1 = [x for x in sim.models if 'Regulating Transformer 1' in x.DEV_TITLE][0]
    tap = regulator1.Tap_Setting
    regulator1.Tap_Setting = '0.99'

    cap1Index = [i for i in range(len(sim.models)) if sim.models[i].NUMERIC_ID == '26'][0]
    sim.models[cap1Index] = Capacitor(sim.models[cap1Index])
    capacitor1 = sim.models[cap1Index]
    isClosed = capacitor1.isClosed
    capacitor1.isClosed = False

    index = [i for i in range(len(sim.models)) if sim.models[i].NUMERIC_ID == '69'][0]
    sim.models[index] = UtilityPV(sim.models[index])
    pv = sim.models[index]
    phaseAngle = pv.PhaseAngle
    pv.PhaseAngle = '65'

    sim.saveAs('Edited New Sim.NMT')

