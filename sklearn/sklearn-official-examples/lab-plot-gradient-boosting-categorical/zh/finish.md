# 总结

在本实验中，我们使用艾姆斯房屋数据集比较了四种不同的管道，用于处理梯度提升估计器中的分类特征。我们发现，丢弃分类特征会导致较差的预测性能，而使用分类特征的三个模型具有可比的错误率。对分类特征进行独热编码是迄今为止最慢的方法，而将分类特征视为有序值并使用直方图梯度提升回归器（HistGradientBoostingRegressor）估计器的原生分类支持具有相似的拟合时间。当分割总数受到限制时，原生分类支持策略表现最佳。
