import numpy as np
import matplotlib.pyplot as plt
import argparse
from InputFile import *

# Problem setup
parser  = argparse.ArgumentParser(description='Input filename');
parser.add_argument('inputfilename',\
                    metavar='inputfilename',type=str,\
                    help='Filename of the input file')
args   = parser.parse_args()
inputs = InputFile(args);
inputs.printInputs();
