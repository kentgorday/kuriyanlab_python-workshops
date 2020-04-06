# Calculate the center of mass coordinates for each residue in each frame of a trajectory.

import sys
import numpy as np
import mdtraj as md

if len(sys.argv) != 3:
    print("Please supply the input PDB/HDF5 as the first argument and the output PDB/HDF5 as the second argument.")
    raise ValueError("wrong number of arguments")

# Load the input trajectory,
# which we assume contains both trajectory and topology information
# (eg PDB/HDF5 formats, determined using the file extension):
fatraj = md.load(sys.argv[1])

# Select a single atom name per residue to represent the center of mass,
# eg CA for protein residues, MG for Magnesium ions,
# and C5 for nucleotide ligands and DNA/RNA residues.
# This could also be modified to include other ligands.
comtop = fatraj.topology.subset(fatraj.topology.select("name CA or name MG or name C5"))

# Create a NumPy array to hold the center of mass coordinates (xyz)
# for each residue in each frame:
comxyz = np.empty((fatraj.n_frames, fatraj.n_residues, 3))

# Loop through residues and calculate the mass-weighted center of mass
# over all atoms:
for j, fares in enumerate(fatraj.topology.residues):
    comxyz[:,j,:] = np.average(fatraj.xyz[:,[atom.index for atom in fares.atoms],:],
                               weights = [atom.element.mass for atom in fares.atoms],
                               axis = 1)

# Create a new Trajectory object from the center of mass coordinates
# and trimmed topology, then save:
comtraj = md.Trajectory(comxyz, comtop)
comtraj.save(sys.argv[2])
