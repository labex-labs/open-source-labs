# Introduction

In this lab, we will demonstrate how to robustly fit a linear model to faulty data using the RANSAC algorithm in scikit-learn. The ordinary linear regressor is sensitive to outliers, and the fitted line can easily be skewed away from the true underlying relationship of data. The RANSAC regressor automatically splits the data into inliers and outliers, and the fitted line is determined only by the identified inliers. We will use the make_regression dataset from scikit-learn to generate random data with outliers, and then fit both a linear model and a RANSAC regressor to the data.

> You can open the `plot-ransac.ipynb` in WebIDE to start the exercises. Learn how to use [Jupyter Notebooks in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks).
> ![](https://file.labex.io/upload/u/1991/fzLMg1oHuQrI.png)
> We can not verify your answers automatically in this lab.

