# Introduction

This lab illustrates how to apply different preprocessing and feature extraction pipelines to different subsets of features, using `ColumnTransformer`. This is particularly handy for the case of datasets that contain heterogeneous data types, since we may want to scale the numeric features and one-hot encode the categorical ones.

In this lab, we will be using the Titanic dataset from OpenML to build a pipeline that preprocesses both categorical and numeric data using `ColumnTransformer` and use that to train a logistic regression model.

> You can open the `plot-column-transformer-mixed-types.ipynb` in WebIDE to start the exercises. Learn how to use [Jupyter Notebooks in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks).
> ![](https://file.labex.io/upload/u/1991/fzLMg1oHuQrI.png)
> We can not verify your answers automatically in this lab.

