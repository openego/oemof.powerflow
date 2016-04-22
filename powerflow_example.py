# base on oemof v0.0.5 !

from oemof_powerflow import Bus, Generator, EnergySystem

my_es = EnergySystem()

my_bus = Bus(uid="bus1")
my_generator = Generator(uid="gen1")

my_es.print_entities()
# just ignore the ExcessSlack object for now

my_es.calculate_powerflow()
