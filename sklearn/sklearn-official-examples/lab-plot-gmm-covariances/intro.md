# Introduction

This tutorial demonstrates the use of different covariance types for Gaussian mixture models (GMMs). GMMs are often used for clustering, and we can compare the obtained clusters with the actual classes from the dataset. We initialize the means of the Gaussians with the means of the classes from the training set to make this comparison valid. We plot predicted labels on both training and held-out test data using a variety of GMM covariance types on the iris dataset. We compare GMMs with spherical, diagonal, full, and tied covariance matrices in increasing order of performance.

Although one would expect full covariance to perform best in general, it is prone to overfitting on small datasets and does not generalize well to held-out test data.

On the plots, train data is shown as dots, while test data is shown as crosses. The iris dataset is four-dimensional. Only the first two dimensions are shown here, and thus some points are separated in other dimensions.

> You can open the `plot-gmm-covariances.ipynb` in WebIDE to start the exercises. Learn how to use [Jupyter Notebooks in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks).
> ![](https://file.labex.io/upload/u/1991/fzLMg1oHuQrI.png)
> We can not verify your answers automatically in this lab.
