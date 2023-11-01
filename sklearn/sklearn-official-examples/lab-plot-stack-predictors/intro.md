# Introduction

In this lab, we will be using the Stacking method to blend several estimators to make predictions. In this strategy, some estimators are individually fitted on some training data while a final estimator is trained using the stacked predictions of these base estimators. We will be using the Ames Housing dataset to predict the final logarithmic price of the houses. We will use 3 learners, linear and non-linear and use a ridge regressor to combine their outputs together. We will also compare the performance of each individual predictor as well as of the stack of the regressors.

> You can open the `plot-stack-predictors.ipynb` in WebIDE to start the exercises. Learn how to use [Jupyter Notebooks in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks).
> ![](https://file.labex.io/upload/u/1991/fzLMg1oHuQrI.png)
> We can not verify your answers automatically in this lab.
