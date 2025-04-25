# 总结

本实验展示了如何使用 scikit-learn 中的 `BayesianGaussianMixture` 类来拟合一个包含三个高斯分布混合的玩具数据集。该类可以使用浓度先验自动调整其混合成分的数量，浓度先验通过 `weight_concentration_prior_type` 参数指定。本实验展示了在选择具有非零权重的成分数量时，使用狄利克雷分布先验和狄利克雷过程先验之间的差异。
