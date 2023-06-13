# Introduction

This lab demonstrates how to use the scikit-learn `BayesianGaussianMixture` class to fit a toy dataset containing a mixture of three Gaussians. The class can adapt its number of mixture components automatically using a concentration prior, which is specified using the `weight_concentration_prior_type` parameter. This lab shows the difference between using a Dirichlet distribution prior and a Dirichlet process prior to select the number of components with non-zero weights.

> You can write code in `lab.ipynb`.
