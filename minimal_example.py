# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 13:34:13 2016

@author: christianfleischer
"""

from __future__ import print_function, division

import pypsa

import numpy as np

network = pypsa.Network()

#add buses
network.add("Bus","bus_1",v_nom=20.)
network.add("Bus","bus_2",v_nom=20.)

#add lines
network.add("Line","line_1_2", bus0="bus_1", bus1="bus_2", x=0.1) 

#add generators
network.add("Generator", "gen_1", bus="bus_1", p_set=100)

#add load
network.add("Load", "load_1", bus="bus_2", p_set=100)

#calculate power flow
network.pf()

print(network.lines_t.p0)

print(network.buses_t.v_mag_pu)
