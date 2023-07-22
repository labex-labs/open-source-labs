# Introduction

Principal Component Regression (PCR) and Partial Least Squares Regression (PLS) are two methods used in regression analysis. PCR involves applying PCA to training data, followed by training a regressor on the transformed samples. The PCA transformation is unsupervised, meaning that no information about the targets is used. As a result, PCR may perform poorly in some datasets where the target is strongly correlated with directions that have low variance.

PLS is both a transformer and a regressor, and it is quite similar to PCR. It also applies a dimensionality reduction to the samples before applying a linear regressor to the transformed data. The main difference with PCR is that the PLS transformation is supervised. Therefore, it does not suffer from the issue mentioned above.

In this lab, we will compare PCR and PLS on a toy dataset.

> You can write code in `plot-pcr-vs-pls.ipynb`.
