# 简介

在本实验中，我们将使用艾姆斯房屋数据集（Ames Housing dataset）来比较梯度提升估计器（Gradient Boosting estimators）中处理分类特征的不同方法。该数据集包含数值特征和分类特征，目标是房屋的销售价格。我们将比较四种不同管道（pipeline）的性能：

- 丢弃分类特征
- 对分类特征进行独热编码（One-hot encoding）
- 将分类特征视为有序值
- 在梯度提升估计器中使用原生分类支持

我们将使用交叉验证（cross-validation）根据拟合时间和预测性能来评估这些管道。

## 虚拟机提示

虚拟机启动完成后，点击左上角切换到“笔记本”（**Notebook**）标签页，以访问Jupyter Notebook进行练习。

有时，你可能需要等待几秒钟让Jupyter Notebook完成加载。由于Jupyter Notebook的限制，操作验证无法自动化。

如果你在学习过程中遇到问题，可以随时向Labby提问。课程结束后提供反馈，我们会及时为你解决问题。
