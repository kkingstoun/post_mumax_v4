import parameters
from fmrmodes import FMRModes
from ovf import OvfFile

if __name__ == "__main__":
    parms = parameters.ovfParms(head="m_y",comp=0)

    mtzyxc = OvfFile(r"C:/Users/Mateusz/Desktop/Radek/circular_10.out", parms)

    vm = FMRModes(mtzyxc, eachX=False, eachY=False)
    vm.calculateModes()
