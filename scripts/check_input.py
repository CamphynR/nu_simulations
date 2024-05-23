
import time
import os
import numpy as np
import argparse
import matplotlib.pyplot as plt
import h5py
from NuRadioMC.utilities.plotting import plot_vertex_distribution
from NuRadioReco.utilities import units

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog = "%(prog)s",
        description = "Script to plot input files"
    )
    parser.add_argument(dest = "filename",
                        help = "input.hdf5 file")
    args = parser.parse_args()

    fin = h5py.File(args.filename, "r")

    print("The input file contains the keys:")
    print("---------------------------------")
    for key in fin.keys():
        print(key)
    print("---------------------------------")

    print("There are the following keys in the file attributes:")
    print("----------------------------------------------------")
    for key in fin.attrs.keys():
        print(key)
    print("----------------------------------------------------")

    # plotting the vertex positions
    xx = np.array(fin["xx"]) 
    yy = np.array(fin["yy"]) 
    zz = np.array(fin["zz"]) 
    E = np.array(fin["energies"])

fig, ax = plot_vertex_distribution(xx,yy,zz, weights = E,
                                   rmax = fin.attrs["rmax"],
                                   zmin = fin.attrs["zmin"])
ax.set_title("weights are replaced with energy")
plt.show()