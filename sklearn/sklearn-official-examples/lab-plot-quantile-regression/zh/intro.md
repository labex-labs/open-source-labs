# 简介

本教程将演示如何使用scikit-learn执行分位数回归。我们将生成两个合成数据集，以说明分位数回归如何预测非平凡的条件分位数。我们将使用 `QuantileRegressor` 类来估计中位数以及分别固定在5%和95%的低和高分位数。我们将把 `QuantileRegressor` 与 `LinearRegression` 进行比较，并使用平均绝对误差（MAE）和均方误差（MSE）评估它们的性能。

## 虚拟机使用提示

虚拟机启动完成后，点击左上角切换到**笔记本**标签，以访问Jupyter Notebook进行练习。

有时，你可能需要等待几秒钟让Jupyter Notebook完成加载。由于Jupyter Notebook的限制，操作的验证无法自动化。

如果你在学习过程中遇到问题，可以随时向Labby提问。课程结束后提供反馈，我们会及时为你解决问题。
