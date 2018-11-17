import numpy as np
import matplotlib.pyplot as plt

def RandomGaussians(x):
    samples,dimn = x.shape;
    numcent      = 3;
    np.random.seed(1)
    x0  = np.random.uniform(0.2,0.8,[numcent,dimn]);
    amp = np.random.uniform(0.5,1,numcent);
    sig = np.random.uniform(0.05,0.15,numcent);
    y   = np.zeros(samples)
    for i in range(numcent):
        y += amp[i]*np.exp(-0.5*np.linalg.norm(x-x0[i],axis=1)**2/sig[i]**2);
    return y;

class Function():
    def __init__(self,inputs):
        self.__inputs_       = inputs;
        self.__dimension_    = self.__inputs_.dimension;
        self.__functionStr_  = self.__inputs_.function;
        self.setFunction()
    def setFunction(self):
        if (self.__functionStr_ == 'RandomGaussians'):
            self.__function_     = RandomGaussians;
        else:
            print("Function type not implemented");
    def evaluate(self,x):
        return self.__function_(x);
    def visualize(self,fig):
        # NOTE: this is only valid for a function with 2 input variables
        x     = np.linspace(0,1,50);
        xx,yy = np.meshgrid(x,x);
        X     = np.vstack([ xx.ravel() , yy.ravel() ]).T;
        z     = self.evaluate(X)
        plt.contourf(xx,yy,np.reshape(z,[50,50]),20,cmap=plt.get_cmap('coolwarm'));
        plt.colorbar();
        plt.show()
        
