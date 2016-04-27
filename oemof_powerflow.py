# base on oemof v0.0.5 !

from oemof.core.energy_system import EnergySystem as OemofEnergySystem
from oemof.core.network.entities import Bus as OemofBus, Component as OemofComponent

class Bus(OemofBus):
    
    # add attribures necessary for pypsa (use talking names)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.list_name = kwargs.get("list_name", None)    
        self.name = kwargs.get("name", None)
        self.nominal_voltage = kwargs.get("v_nom", None)

class Generator(OemofComponent):
    
    # add attribures necessary for pypsa (use talking names)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.list_name = kwargs.get("list_name", None)
        self.name = kwargs.get("name", None)
        self.bus = kwargs.get("bus", None)
        self.active_power_setpoint = kwargs.get("p_set", None)

class Load(OemofComponent):
    
    # add attribures necessary for pypsa (use talking names)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.list_name = kwargs.get("list_name", None)
        self.name = kwargs.get("name", None)
        self.bus = kwargs.get("bus", None)
        self.active_power_setpoint = kwargs.get("p_set", None)

class Line(OemofComponent):
    
    # add attribures necessary for pypsa (use talking names)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.list_name = kwargs.get("list_name", None)
        self.name = kwargs.get("name", None)
        self.bus0 = kwargs.get("bus0", None)
        self.bus1 = kwargs.get("bus1", None)
        self.active_power_setpoint = kwargs.get("p_set", None)
        
        
class EnergySystem(OemofEnergySystem):

    def print_entities(self):
        print(self.entities)

    # add mehtod for powerflow calculation based on generators, buses etc. from
    # energy system
    def calculate_powerflow(self):
        print("Here starts the magic")
