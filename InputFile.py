import numpy as np
from pprint import pprint

# Auxiliary class for packaging input file options
class InputFile():
    def __init__(self,args=[]):
        print args
        if (args.inputfilename == []):
            inputfilename    = 'input.dat'
        else:
            inputfilename    = args.inputfilename
        inputfilestream      = open(inputfilename)
        self.projdir         = inputfilestream.readline().strip().split('= ')[1];
        self.datadir         = inputfilestream.readline().strip().split('= ')[1];
        inputfilestream.close();
    def printInputs(self):
        pprint(vars(self));
