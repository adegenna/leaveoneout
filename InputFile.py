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
        self.outdir          = inputfilestream.readline().strip().split('= ')[1];
        self.function        = inputfilestream.readline().strip().split('= ')[1];
        self.dimension       = int(inputfilestream.readline().strip().split('= ')[1]);
        self.initialSamples  = int(inputfilestream.readline().strip().split('= ')[1]);
        inputfilestream.close();
    def printInputs(self):
        attrs = vars(self);
        print('\n');
        print("********************* INPUTS *********************")
        print '\n'.join("%s: %s" % item for item in attrs.items())
        print("**************************************************")
        print('\n');
