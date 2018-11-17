import numpy as np
import matplotlib.pyplot as plt
import argparse
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, ConstantKernel as C
from InputFile import *
from Data import *
from Function import *
from Sampler import *

# Problem setup
parser  = argparse.ArgumentParser(description='Input filename');
parser.add_argument('inputfilename',\
                    metavar='inputfilename',type=str,\
                    help='Filename of the input file')
args   = parser.parse_args()
inputs = InputFile(args);
inputs.printInputs();

# Setup visualization grid (only valid for 2D input parameter space)
x     = np.linspace(0,1,50);
xx,yy = np.meshgrid(x,x);
X     = np.vstack([ xx.ravel() , yy.ravel() ]).T

# Construct needed objects
dataPoints   = Data(inputs);
trueFunction = Function(inputs);
sampler      = Sampler(inputs,dataPoints,trueFunction);

# Visualize ground truth (only valid for 2D data)
fig = plt.figure(1); plt.ion();
plt.subplot(131);
Z   = trueFunction.evaluate(X)
plt.contourf(xx,yy,np.reshape(Z,[50,50]),20,vmin=0,vmax=1.0,cmap=plt.get_cmap('coolwarm'));
plt.gca().set_aspect('equal');

# Initial coarse random sampling + build base GP
sampler.uniform(samples=inputs.initialSamples);
sampler.buildBaseGP();

# Visualize initial results (only valid for 2D data)
plt.subplot(132);
Z           = sampler.predictWithCurrentSurrogate(X);
xcent,zcent = dataPoints.getData();
plt.contourf(xx,yy,np.reshape(Z,[50,50]),20,vmin=0,vmax=1.0,cmap=plt.get_cmap('coolwarm'));
plt.plot(xcent[:,0],xcent[:,1],'ko');
plt.gca().set_aspect('equal');
plt.show();

# Adaptive sampling
sampler.leaveOneOutAdaptive();

# Visualize final results (only valid for 2D data)
Z           = sampler.predictWithCurrentSurrogate(X);
xcent,zcent = dataPoints.getData();
plt.subplot(133);
plt.contourf(xx,yy,np.reshape(Z,[50,50]),20,vmin=0,vmax=1.0,cmap=plt.get_cmap('coolwarm'));
plt.plot(xcent[:,0],xcent[:,1],'ko');
plt.gca().set_aspect('equal');
plt.ioff();
plt.show();
