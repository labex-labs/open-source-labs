# Introduction

In this lab, we will explore how model complexity influences both prediction accuracy and computational performance. We will be using two datasets - Diabetes Dataset for regression and 20newsgroups Dataset for classification. We will model the complexity influence on three different estimators:

- SGDClassifier (for classification data) which implements stochastic gradient descent learning
- NuSVR (for regression data) which implements Nu support vector regression
- GradientBoostingRegressor builds an additive model in a forward stage-wise fashion

We will vary the model complexity through the choice of relevant model parameters in each of our selected models. Next, we will measure the influence on both computational performance (latency) and predictive power (MSE or Hamming Loss).

> You can open the `plot-model-complexity-influence.ipynb` in WebIDE to start the exercises. Learn how to use [Jupyter Notebooks in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks).
> ![](https://file.labex.io/upload/u/1991/fzLMg1oHuQrI.png)
> We can not verify your answers automatically in this lab.
