# 总结

本实验展示了如何使用分位数回归，通过 scikit-learn 创建预测区间。我们为一个回归问题生成了合成数据，对其应用函数，并使用对数正态分布创建目标观测值。我们将数据拆分为训练集和测试集，拟合非线性分位数和最小二乘回归器，并创建了一个均匀分布的输入值评估集，其范围为[0, 10]。我们比较了预测中位数和预测均值，分析了误差指标，并校准了置信区间。最后，我们调整了分位数回归器的超参数。
