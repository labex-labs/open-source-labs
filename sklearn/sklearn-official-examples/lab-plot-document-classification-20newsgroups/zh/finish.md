# 总结

本实验展示了如何使用 scikit-learn 将文本文档分类到不同类别中。我们加载了 20 新闻组数据集，并使用词袋方法和 TF-IDF 加权的文档 - 词项稀疏矩阵对特征进行编码。我们对分类器进行了两次训练，一次在包含元数据的文本样本上进行，另一次在去除元数据之后进行。我们使用混淆矩阵分析了测试集上的分类错误，并检查了定义训练模型分类函数的系数。我们还使用八个不同的分类模型对数据集进行了训练和测试，并获得了每个模型的性能结果。本研究的目的是突出针对此类多类别文本分类问题，不同类型分类器在计算量/准确性方面的权衡。
