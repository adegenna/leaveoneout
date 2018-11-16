import numpy as np

# Class to handle data samples
class Data():
    def __init__(self,inputs):
        self.__inputs_     = inputs;
        self.__X_          = np.zeros([self.inputs_.initialSamples , self.inputs_.dimension]);
        self.__samples     = self.inputs_.initialSamples;
        self.__dimension_  = self.inputs_.dimension;
    def getData(self):
        # Returns copy of data
        return self.__X_.copy();
    def appendData(self,Xnew):
        self.__X_       = np.vstack([self.__X_ , Xnew]);
        self.__samples_ = self.__X_.shape[0];
    def getNumberSamples(self):
        return self.__samples_;
