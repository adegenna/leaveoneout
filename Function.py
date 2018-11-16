import numpy as np

# Class to handle data samples
class Function():
    def __init__(self,inputs):
        self.__inputs_       = inputs;
        self.__dimension_    = self.inputs_.dimension;
        self.__functionStr_  = self.inputs_.function;
        self.setFunction()
    def setFunction(self):
        if (self.__function_ == 'RandomGaussians'):
            self.__function = RandomGaussian(self.__dimension);
        else:
            print("Not implemented");
