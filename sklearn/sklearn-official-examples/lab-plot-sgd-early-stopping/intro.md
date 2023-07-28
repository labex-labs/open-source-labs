# Introduction

Stochastic Gradient Descent is a popular optimization technique used for minimizing a loss function. The technique performs gradient descent step by step in a stochastic manner, i.e., by randomly selecting samples for each iteration. The method is efficient, especially for fitting linear models. However, convergence is not guaranteed at each iteration, and the loss function may not necessarily decrease at each iteration. In this case, monitoring the convergence on the loss function can be difficult. In this lab, we will explore the early stopping strategy, which is an approach for monitoring convergence on a validation score. We will use the `SGDClassifier` model from the scikit-learn library and the MNIST dataset to illustrate how early stopping can be used to achieve almost the same accuracy as compared to a model built without early stopping, and significantly reduce training time.

> You can write code in `plot-sgd-early-stopping.ipynb`.
