# 总结

本实验在二维数据集上比较了不同的异常检测算法。这些数据集包含一种或两种模式（高密度区域），以说明算法处理多模态数据的能力。除了局部离群因子（LOF）外，内点和离群点之间的决策边界以黑色显示，因为在用于离群点检测时，它没有可应用于新数据的预测方法。发现 :class:`~sklearn.svm.OneClassSVM` 对离群点敏感，因此在离群点检测方面表现不是很好。:class:`sklearn.linear_model.SGDOneClassSVM` 是基于随机梯度下降（SGD）的一类支持向量机（One-Class SVM）的实现。:class:`sklearn.covariance.EllipticEnvelope` 假设数据是高斯分布的，并学习一个椭圆，并且 :class:`~sklearn.ensemble.IsolationForest` 和 :class:`~sklearn.neighbors.LocalOutlierFactor` 对于多模态数据集似乎表现得相当不错。
