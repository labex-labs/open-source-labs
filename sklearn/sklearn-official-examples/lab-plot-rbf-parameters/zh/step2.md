# 训练分类器

- 使用 `np.logspace` 创建 `gamma` 和 `C` 参数的对数网格。
- 使用 `StratifiedShuffleSplit` 将数据拆分为训练集和测试集。
- 使用 `GridSearchCV` 进行网格搜索，以找到支持向量机（SVM）模型的最佳参数。
- 为二维版本中的所有参数拟合一个分类器。
