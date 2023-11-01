# Introduction

This lab will demonstrate how to use polynomial kernel approximation in scikit-learn to efficiently generate polynomial kernel feature-space approximations. This is used to train linear classifiers that approximate the accuracy of kernelized ones. We will be using the Covtype dataset, which contains 581,012 samples with 54 features each, distributed among 6 classes. The goal of this dataset is to predict forest cover type from cartographic variables only (no remotely sensed data). After loading, we transform it into a binary classification problem to match the version of the dataset in the LIBSVM webpage, which was the one used in the original paper.

> You can open the `plot-scalable-poly-kernels.ipynb` in WebIDE to start the exercises. Learn how to use [Jupyter Notebooks in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks).
> ![](https://file.labex.io/upload/u/1991/fzLMg1oHuQrI.png)
> We can not verify your answers automatically in this lab.
