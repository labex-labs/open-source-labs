# Introduction

In this lab, we will be using the Ames Housing dataset to compare different methods of handling categorical features in Gradient Boosting estimators. The dataset contains both numerical and categorical features, and the target is the sales price of the houses. We will compare the performance of four different pipelines:

- Dropping the categorical features
- One-hot encoding the categorical features
- Treating the categorical features as ordinal values
- Using native categorical support in the Gradient Boosting estimator

We will evaluate the pipelines in terms of their fit times and prediction performances using cross-validation.

> You can open the `plot-gradient-boosting-categorical.ipynb` in WebIDE to start the exercises. Learn how to use [Jupyter Notebooks in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks).
> ![](https://file.labex.io/upload/u/1991/fzLMg1oHuQrI.png)
> We can not verify your answers automatically in this lab.

