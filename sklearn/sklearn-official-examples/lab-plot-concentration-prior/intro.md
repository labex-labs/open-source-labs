# Introduction

This lab demonstrates how to use the scikit-learn `BayesianGaussianMixture` class to fit a toy dataset containing a mixture of three Gaussians. The class can adapt its number of mixture components automatically using a concentration prior, which is specified using the `weight_concentration_prior_type` parameter. This lab shows the difference between using a Dirichlet distribution prior and a Dirichlet process prior to select the number of components with non-zero weights.

> You can open the `plot-concentration-prior.ipynb` in WebIDE to start the exercises. Learn how to use [Jupyter Notebooks in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks).
> ![](https://file.labex.io/upload/u/1991/fzLMg1oHuQrI.png)
> Labby cannot automatically verify the answers because it cannot access the notebook.
