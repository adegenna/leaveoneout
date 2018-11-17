import numpy as np

# Class to handle data samples
class Data():
    def __init__(self,inputs):
        self.__inputs_     = inputs;
        self.__X_          = np.empty((0 , self.__inputs_.dimension), float);
        self.__Z_          = np.empty((0), float);
        self.__samples     = self.__inputs_.initialSamples;
        self.__dimension_  = self.__inputs_.dimension;
    def getData(self):
        # Returns copy of data
        return self.__X_.copy() , self.__Z_.copy();
    def appendData(self,Xnew,Znew):
        self.__X_       = np.vstack([self.__X_ , Xnew]);
        self.__Z_       = np.append(self.__Z_ , Znew);
        self.__samples_ = self.__X_.shape[0];
    def getNumberSamples(self):
        return self.__samples_;
