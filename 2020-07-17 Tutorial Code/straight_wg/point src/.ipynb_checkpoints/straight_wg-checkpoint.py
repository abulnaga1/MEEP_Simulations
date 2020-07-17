import meep as mp
import pickle

#Create a 16um x 8um computational cell (2D)
cell = mp.Vector3(16,8,0)

#Define a fixed-index rectangle as our waveguide
geometry = [mp.Block(mp.Vector3(mp.inf,1,mp.inf),
                     center=mp.Vector3(),
                     material=mp.Medium(epsilon=12))]

#Define a CW fixed frequency point source with frequency 0.15 (units of 2*pi*c) --> vacuum lambda = 1/freq = 6.67um
#Source is polarized out of the plane (z), and is located 1um from the edge of the simulation boundary
sources = [mp.Source(mp.ContinuousSource(frequency=0.15),
                     component=mp.Ez,
                     center=mp.Vector3(-7,0))]

#Add PML layer around the boundary (thickness = 1um)
pml_layers = [mp.PML(1.0)]

#Define a resolution of 10 pixels per um (100nm resolution)
resolution = 10

#Define the simulation using our structures
sim = mp.Simulation(cell_size=cell,
                    boundary_layers=pml_layers,
                    geometry=geometry,
                    sources=sources,
                    resolution=resolution)

#Set the run time
sim.run(until=200)

eps_data = sim.get_array(center=mp.Vector3(), size=cell, component=mp.Dielectric)
ez_data = sim.get_array(center=mp.Vector3(), size=cell, component=mp.Ez)

f = open('output.pckl', 'wb')
pickle.dump([eps_data, ez_data], f)
f.close()