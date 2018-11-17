import numpy as np
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, ConstantKernel as C

class Sampler():
    def __init__(self,inputs,data,function):
        self.__inputs_      = inputs;
        self.__data_        = data;
        self.__function_    = function;
        self.__adaptiveIters_ = inputs.adaptiveIters;
        self.__testSamples_   = inputs.testSamples;
        self.__kernel_        = C(inputs.kernelScale, (1e-3, 1e3)) * RBF(inputs.kernelSigma, (1e-2, 1e2))
        self.generateTestPoints();
    def uniform(self,samples):
        x = np.random.uniform(0,1,[ samples , self.__inputs_.dimension ])
        z = self.__function_.evaluate(x);
        self.__data_.appendData(x,z);
    def generateTestPoints(self):
        self.__Xtest_ = np.random.uniform(0,1,[self.__testSamples_,self.__inputs_.dimension]);
    def buildBaseGP(self):
        xdata,zdata     = self.__data_.getData();
        self.__gpbase_  = GaussianProcessRegressor(kernel=self.__kernel_, n_restarts_optimizer = 9);
        self.__gpbase_.fit(xdata,zdata);
    def buildLeaveOneOutGP(self,idx):
        xdata,zdata  = self.__data_.getData();
        x_i          = xdata[np.arange(xdata.shape[0]) != idx];
        z_i          = zdata[np.arange(xdata.shape[0]) != idx];
        gp_i         = GaussianProcessRegressor(kernel=self.__kernel_, n_restarts_optimizer = 9);
        gp_i.fit(x_i,z_i);
        return gp_i;
    def addNewSample(self,error):
        idx         = np.argmax(error);
        epsilon     = np.random.uniform(0,0.1,self.__inputs_.dimension);
        xdata,zdata = self.__data_.getData();
        xnew        = xdata[idx] + epsilon;
        znew        = self.__function_.evaluate(np.expand_dims(xnew,axis=0));
        self.__data_.appendData(xnew,znew);
    def leaveOneOutAdaptive(self):
        print("********************* ADAPTIVE SAMPLING *********************")
        for i in range(self.__adaptiveIters_):
            print("iteration " + str(i+1) + " / " + str(self.__adaptiveIters_) + "... ");
            # Calculate base predictions
            self.buildBaseGP();
            zpred_base, sig_base = self.__gpbase_.predict(self.__Xtest_, return_std=True)
            samples = self.__data_.getNumberSamples();
            error   = np.zeros(samples);
            for j in range(samples):
                # Calculate leave-one-out predictions
                gp_j           = self.buildLeaveOneOutGP(j);
                zpred_j, sig_j = gp_j.predict(self.__Xtest_, return_std=True)
                # Compare base to leave-one-out
                error[j] = np.linalg.norm( zpred_base - zpred_j );
            # Add new point
            self.addNewSample(error);
            print("done.")
    def predictWithCurrentSurrogate(self,x):
        z = self.__gpbase_.predict(x);
        return z;
            
