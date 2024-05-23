import os
from NuRadioReco.utilities import units
from NuRadioMC.EvtGen.generator import generate_eventlist_cylinder
import argparse

if __name__ == "__main__":
    input_dir = "input_files"
    if not os.path.exists(input_dir):
        os.mkdir(input_dir)

    parser = argparse.ArgumentParser(
        prog = "%(prog)s",
        description= "File to create neutrino events used as input for NuRadioMC sim"
    )

    parser.add_argument("--nr_events", "-n",
                        type = int,
                        default = 1000,
                        help = "number of neutrino events to be generated")
    parser.add_argument("--Energy_min", "-E_min",
                        type = float,
                        default= 1e16 * units.eV,
                        dest = "E_min",
                        help = "lower bound on energy of generated events")
    parser.add_argument("--Energy_max", "-E_max",
                        type = float,
                        default = 1e20 * units.eV,
                        dest = "E_max",
                        help = "upper bound on energy of generated events")
args = parser.parse_args()

volume = {
    "fiducial_rmin" : 0 * units.km,
    "fiducial_rmax": 4 * units.km,
    "fiducial_zmin": -3 * units.km,
    "fiducial_zmax": 0 * units.km,
}

flavor = [12, -12, 14, -14, 16, -16]

proposal = False
proposal_config = "Greenland"

filename = f"{input_dir}/input_{args.E_min:.1e}_{args.E_max:.1e}.hdf5"

generate_eventlist_cylinder(filename, args.nr_events, args.E_min, args.E_max,
                            volume,
                            flavor = flavor,
                            proposal = proposal, proposal_config=proposal_config,
                            proposal_tables_path= "./tables",)