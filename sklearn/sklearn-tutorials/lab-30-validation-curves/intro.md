# Introduction

In machine learning, every estimator has its advantages and drawbacks. The generalization error of an estimator can be decomposed into bias, variance, and noise. The bias of an estimator is the average error for different training sets, while the variance indicates its sensitivity to varying training sets. Noise is a property of the data.

In this lab, we will explore how to use validation curves to evaluate the performance of machine learning models. Validation curves allow us to plot the influence of a single hyperparameter on the training score and the validation score, helping us determine if the model is overfitting or underfitting for different hyperparameter values.

> You can write code in `30-validation-curves.ipynb`.
