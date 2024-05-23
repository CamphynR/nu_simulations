from NuRadioReco.utilities import units
from NuRadioMC.EvtGen.generator import generate_eventlist_cylinder
import argparse

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
                    help = "lower bound on energy of generated events")
parser.add_argument("--Energy_max", "-E_max",
                    type = float,
                    default = 1e20 * units.eV,
                    help = "upper bound on energy of generated events")

