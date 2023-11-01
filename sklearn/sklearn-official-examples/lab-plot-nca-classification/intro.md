# Introduction

This lab will show how to compare nearest neighbors classification with and without Neighborhood Components Analysis (NCA). We will plot the class decision boundaries given by a Nearest Neighbors classifier when using the Euclidean distance on the original features, versus using the Euclidean distance after the transformation learned by Neighborhood Components Analysis. The latter aims to find a linear transformation that maximizes the (stochastic) nearest neighbor classification accuracy on the training set. We will use the Iris dataset which contains 3 classes of 50 instances each.

> You can open the `plot-nca-classification.ipynb` in WebIDE to start the exercises. Learn how to use [Jupyter Notebooks in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks).
> ![](https://file.labex.io/upload/u/1991/fzLMg1oHuQrI.png)
> Labby cannot automatically verify the answers because it cannot access the notebook.
