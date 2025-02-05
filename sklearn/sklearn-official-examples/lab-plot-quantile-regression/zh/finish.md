# 总结

在本教程中，我们学习了如何使用scikit-learn进行分位数回归。我们生成了两个合成数据集，以说明分位数回归如何预测非平凡的条件分位数。我们使用 `QuantileRegressor` 类来估计中位数以及分别固定在5%和95%的低分位数和高分位数。我们将 `QuantileRegressor` 与 `LinearRegression` 进行了比较，并使用平均绝对误差（MAE）和均方误差（MSE）评估了它们的性能。
