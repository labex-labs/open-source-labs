# 拟合模型并评估测试准确率

通过使用`model.transform()`对训练数据集和测试数据集进行转换，并在转换后的训练数据集上拟合 K 近邻分类器，来拟合每个模型并评估测试准确率。使用`knn.score()`计算转换后的测试数据集上的最近邻准确率。
