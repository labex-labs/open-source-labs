# Introduction

In this lab, we will explore the use of robust covariance estimation with Mahalanobis distances on Gaussian distributed data. Mahalanobis distance is a measure of the distance between a point and a distribution. It is defined as the distance between a point and the mean of the distribution, scaled by the inverse of the covariance matrix of the distribution. For Gaussian distributed data, the Mahalanobis distance can be used to compute the distance of an observation to the mode of the distribution. We will compare the performance of the Minimum Covariance Determinant (MCD) estimator, a robust estimator of covariance, with the standard covariance Maximum Likelihood Estimator (MLE) in calculating the Mahalanobis distances of a contaminated dataset.

> You can write code in `lab.ipynb`.
