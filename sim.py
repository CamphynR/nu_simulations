import argparse
import os
from NuRadioMC.simulation import simulation

if __name__ == "__main__":
    results_folder = "results"
    if not os.path.exists(results_folder):
        os.mkdir(results_folder)

    parser = argparse.ArgumentParser(
        prog = "%(prog)s",
        description = "File to run NuRadioMC simulation"
    )
    parser.add_argument("--input", "-i",
                        help = ".hdf5 file created by the event generation")
    parser.add_argument("--detector", "-d",
                        help = "Detector configuration JSON file")
    parser.add_argument("--config", "-c",
                        help = "Config YAML file containing sim settings")
    parser.add_argument("-o", "--output",
                        default = os.path.join(results_folder, "sim_test.hdf5"),
                        type = str,
                        help = "Filename given to output sim file")
    args = parser.parse_args()


    class MlSimulation(simulation.simulation):
        def _detector_simulation(self):
            pass

    sim  = MlSimulation(inputfilename = args.input,
                        outputfilename = args.output,
                        detectorfile = args.detector,
                        config_file = args.config,
                        )

    sim.run()