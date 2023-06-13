# Introduction

This lab illustrates the approximation of the feature map of an RBF kernel using RBFSampler and Nystroem to approximate the feature map of an RBF kernel for classification with an SVM on the digits dataset. Results using a linear SVM in the original space, a linear SVM using the approximate mappings and using a kernelized SVM are compared. Timings and accuracy for varying amounts of Monte Carlo samplings (in the case of RBFSampler, which uses random Fourier features) and different sized subsets of the training set (for Nystroem) for the approximate mapping are shown.

> You can write code in `lab.ipynb`.
