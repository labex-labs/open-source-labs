# Introduction

This tutorial will demonstrate how to perform quantile regression using scikit-learn. We will generate two synthetic datasets to illustrate how quantile regression can predict non-trivial conditional quantiles. We will use the `QuantileRegressor` class to estimate the median as well as a low and high quantile fixed at 5% and 95%, respectively. We will compare `QuantileRegressor` with `LinearRegression` and evaluate their performance using mean absolute error (MAE) and mean squared error (MSE).

> You can write code in `plot-quantile-regression.ipynb`.
