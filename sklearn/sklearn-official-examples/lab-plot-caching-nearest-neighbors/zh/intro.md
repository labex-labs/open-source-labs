# 简介

本实验展示了如何在 KNeighborsClassifier 中使用 k 近邻之前预先计算它们。KNeighborsClassifier 可以在内部计算最近邻，但预先计算它们有几个好处，例如更精细的参数控制、多次使用的缓存或自定义实现。在这里，我们使用管道的缓存属性来缓存 KNeighborsClassifier 多次拟合之间的最近邻图。

## 虚拟机提示

虚拟机启动完成后，点击左上角切换到**笔记本**标签，以访问 Jupyter Notebook 进行练习。

有时，你可能需要等待几秒钟让 Jupyter Notebook 完成加载。由于 Jupyter Notebook 的限制，操作的验证无法自动化。

如果你在学习过程中遇到问题，随时向 Labby 提问。课程结束后提供反馈，我们将立即为你解决问题。
