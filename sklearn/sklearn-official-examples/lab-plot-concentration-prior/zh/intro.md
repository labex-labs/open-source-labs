# 简介

本实验展示了如何使用 scikit-learn 的 `BayesianGaussianMixture` 类来拟合一个包含三个高斯分布混合的玩具数据集。该类可以使用浓度先验自动调整混合成分的数量，浓度先验通过 `weight_concentration_prior_type` 参数指定。本实验展示了在选择具有非零权重的成分数量时，使用狄利克雷分布先验和狄利克雷过程先验之间的区别。

## 虚拟机使用提示

虚拟机启动完成后，点击左上角切换到 **笔记本** 标签页，以访问 Jupyter Notebook 进行练习。

有时，你可能需要等待几秒钟让 Jupyter Notebook 完成加载。由于 Jupyter Notebook 的限制，操作验证无法自动化。

如果你在学习过程中遇到问题，随时向 Labby 提问。课程结束后提供反馈，我们会及时为你解决问题。
