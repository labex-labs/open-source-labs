# Introduction

In this lab, we will demonstrate how to robustly fit a linear model to faulty data using the RANSAC algorithm in scikit-learn. The ordinary linear regressor is sensitive to outliers, and the fitted line can easily be skewed away from the true underlying relationship of data. The RANSAC regressor automatically splits the data into inliers and outliers, and the fitted line is determined only by the identified inliers. We will use the make_regression dataset from scikit-learn to generate random data with outliers, and then fit both a linear model and a RANSAC regressor to the data.

> You can write code in `plot-ransac.ipynb`.
