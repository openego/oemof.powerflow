# base on oemof v0.0.5 !

from oemof_powerflow import Bus, Generator, Line, Load, EnergySystem

import pypsa

network = pypsa.Network()
#my_es = EnergySystem()
#initialize buses
bus_1 = Bus(class_name="Bus", uid="bus_1", v_nom=20.)
bus_2 = Bus(class_name="Bus", uid="bus_2", v_nom=20.)

#initialize generators
gen_1 = Generator(class_name="Generator", uid="gen_1", bus="bus_1", active_power_setpoint=100)

#initialize loads
load_1 = Load(class_name="Load", uid="load_1", bus="bus_2", active_power_setpoint=100)

#initialize lines
line_1 = Line(class_name="Line", uid="line_1", bus0="bus_1", bus1="bus_2", resistance=0.1)


#add buses
#network.add("Bus","bus_1",v_nom=20.)
#network.add("Bus","bus_2",v_nom=20.)
network.add(bus_1.class_name, bus_1.uid, v_nom=bus_1.nominal_voltage)
network.add(bus_2.class_name, bus_2.uid, v_nom=bus_2.nominal_voltage)

#add generators
#network.add("Generator", "gen_1", bus="bus_1", p_set=100)
network.add(gen_1.class_name, gen_1.uid, bus=gen_1.bus, p_set=gen_1.active_power_setpoint)

#add load
#network.add("Load", "load_1", bus="bus_2", p_set=100)
network.add(load_1.class_name, load_1.uid, bus=load_1.bus, p_set=load_1.active_power_setpoint)

#add lines
#network.add("Line","line_1_2", bus0="bus_1", bus1="bus_2", x=0.1) 
network.add(line_1.class_name, line_1.uid, bus0=line_1.bus0, bus1=line_1.bus1, x=line_1.resistance)

network.pf()

print(network.lines_t.p0)

print(network.buses_t.v_mag_pu)

print (gen_1.active_power_setpoint)
#my_es.print_entities()
# just ignore the ExcessSlack object for now

#my_es.calculate_powerflow()
