# base on oemof v0.0.5 !

from oemof_powerflow import Bus, Generator, EnergySystem

import pypsa

network = pypsa.Network()
#my_es = EnergySystem()

bus_1 = Bus(uid="1", list_name="Bus", name="bus_1", v_nom=20.)
bus_2 = Bus(uid="2", list_name="Bus", name="bus_2", v_nom=20.)

print(bus_1)

my_generator = Generator(uid="gen1")

#add buses
network.add(bus_1)
network.add("Bus","bus_1",v_nom=20.)
network.add("Bus","bus_2",v_nom=20.)

#add lines
network.add("Line","line_1_2", bus0="bus_1", bus1="bus_2", x=0.1) 

#add generators
network.add("Generator", "gen_1", bus="bus_1", p_set=100)

#add load
network.add("Load", "load_1", bus="bus_2", p_set=100)

#my_es.print_entities()
# just ignore the ExcessSlack object for now

#my_es.calculate_powerflow()
