# base on oemof v0.0.5 !

from oemof.core.energy_system import EnergySystem as OemofEnergySystem
from oemof.core.network.entities import Bus as OemofBus, Component as OemofComponent

class Generator(OemofComponent):
    # add attribures necessary for pypsa (use talking names)
    pass

class Bus(OemofBus):
    # add attribures necessary for pypsa (use talking names)
    pass

class EnergySystem(OemofEnergySystem):

    def print_entities(self):
        print(self.entities)

    # add mehtod for powerflow calculation based on generators, buses etc. from
    # energy system
    def calculate_powerflow(self):
        print("Here starts the magic")
