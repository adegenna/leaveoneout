import numpy as np
import matplotlib.pyplot as plt
import argparse
from InputFile import *
from Data import *

# Problem setup
parser  = argparse.ArgumentParser(description='Input filename');
parser.add_argument('inputfilename',\
                    metavar='inputfilename',type=str,\
                    help='Filename of the input file')
args   = parser.parse_args()
inputs = InputFile(args);
inputs.printInputs();

# Construct needed objects
dataPoints   = Data(inputs);
trueFunction = Function(inputs);
# sampler      = Sampler(inputs,dataPoints,trueFunction);

# # Initial coarse random sampling
# sampler.uniform(samples=inputs.samples);

# # Adaptive sampling
# sampler.leaveOneOutAdaptive(samples=10);
