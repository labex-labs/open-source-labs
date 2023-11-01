# Introduction

This tutorial will guide you through the process of using kernel approximation techniques in scikit-learn.

Kernel methods, such as support vector machines (SVM), are powerful techniques for non-linear classification. These methods rely on the concept of a kernel function that maps input data into a high-dimensional feature space. However, working with explicit feature mappings can be computationally expensive, especially for large datasets. Kernel approximation methods provide a solution by generating low-dimensional approximations of the kernel feature space.

In this tutorial, we will explore several kernel approximation techniques available in scikit-learn, including the Nystroem method, Radial Basis Function (RBF) kernel approximation, Additive Chi Squared (ACS) kernel approximation, Skewed Chi Squared (SCS) kernel approximation, and Polynomial kernel approximation using Tensor Sketch. We will demonstrate how to use these techniques and discuss their advantages and limitations.

> You can open the `39-kernel-approximation.ipynb` in WebIDE to start the exercises. Learn how to use [Jupyter Notebooks in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks).
> ![](https://file.labex.io/upload/u/1991/fzLMg1oHuQrI.png)
> We can not verify your answers automatically in this lab.

