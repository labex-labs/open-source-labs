# Introduction

Principal Component Regression (PCR) and Partial Least Squares Regression (PLS) are two methods used in regression analysis. PCR involves applying PCA to training data, followed by training a regressor on the transformed samples. The PCA transformation is unsupervised, meaning that no information about the targets is used. As a result, PCR may perform poorly in some datasets where the target is strongly correlated with directions that have low variance.

PLS is both a transformer and a regressor, and it is quite similar to PCR. It also applies a dimensionality reduction to the samples before applying a linear regressor to the transformed data. The main difference with PCR is that the PLS transformation is supervised. Therefore, it does not suffer from the issue mentioned above.

In this lab, we will compare PCR and PLS on a toy dataset.

> You can open the `plot-pcr-vs-pls.ipynb` in WebIDE to start the exercises. Learn how to use [Jupyter Notebooks in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks).
> ![](https://file.labex.io/upload/u/1991/fzLMg1oHuQrI.png)
> Labby cannot automatically verify the answers because it cannot access the notebook.
