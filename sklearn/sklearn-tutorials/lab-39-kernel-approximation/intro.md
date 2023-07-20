# Introduction

This tutorial will guide you through the process of using kernel approximation techniques in scikit-learn.

Kernel methods, such as support vector machines (SVM), are powerful techniques for non-linear classification. These methods rely on the concept of a kernel function that maps input data into a high-dimensional feature space. However, working with explicit feature mappings can be computationally expensive, especially for large datasets. Kernel approximation methods provide a solution by generating low-dimensional approximations of the kernel feature space.

In this tutorial, we will explore several kernel approximation techniques available in scikit-learn, including the Nystroem method, Radial Basis Function (RBF) kernel approximation, Additive Chi Squared (ACS) kernel approximation, Skewed Chi Squared (SCS) kernel approximation, and Polynomial kernel approximation using Tensor Sketch. We will demonstrate how to use these techniques and discuss their advantages and limitations.

> You can write code in `39-kernel-approximation.ipynb`.
