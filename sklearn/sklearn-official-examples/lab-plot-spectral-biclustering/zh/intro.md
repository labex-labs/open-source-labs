# 简介

在本实验中，我们将使用谱双聚类（Spectral Biclustering）算法对数据进行聚类，该算法会同时考虑矩阵的行（样本）和列（特征）。其目的不仅是识别样本之间的模式，还包括样本子集内部的模式，从而能够检测数据中的局部结构。这使得谱双聚类特别适用于特征顺序或排列固定的数据集，如图像、时间序列或基因组数据。我们将使用 scikit-learn 库生成棋盘数据集，并使用谱双聚类算法对其进行双聚类。

## 虚拟机使用提示

虚拟机启动完成后，点击左上角切换到“**笔记本**”标签页，以访问 Jupyter Notebook 进行练习。

有时，你可能需要等待几秒钟让 Jupyter Notebook 完成加载。由于 Jupyter Notebook 的限制，操作验证无法自动化。

如果你在学习过程中遇到问题，随时向 Labby 提问。课程结束后提供反馈，我们会及时为你解决问题。
