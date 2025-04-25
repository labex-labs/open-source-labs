# 简介

在本实验中，我们将学习如何使用信息论标准，通过高斯混合模型（Gaussian Mixture Models，GMM）进行模型选择。模型选择涉及模型的协方差类型和组件数量。我们将使用赤池信息准则（Akaike Information Criterion，AIC）和贝叶斯信息准则（Bayes Information Criterion，BIC）来选择最佳模型。我们将通过对标准正态分布进行随机采样来生成两个组件。一个组件保持球形，但进行了平移和重新缩放。另一个组件则变形为具有更一般的协方差矩阵。

## 虚拟机使用提示

虚拟机启动完成后，点击左上角切换到“笔记本”标签，以访问 Jupyter Notebook 进行练习。

有时，你可能需要等待几秒钟，以便 Jupyter Notebook 完成加载。由于 Jupyter Notebook 的限制，操作验证无法自动化。

如果你在学习过程中遇到问题，请随时向 Labby 提问。课程结束后提供反馈，我们将立即为你解决问题。
