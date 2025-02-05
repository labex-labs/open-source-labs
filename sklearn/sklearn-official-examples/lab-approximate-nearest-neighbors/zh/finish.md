# 总结

在本实验中，我们学习了如何使用 Python 的 scikit-learn 库在 t-SNE 中使用近似最近邻。我们导入了所需的库，为 `nmslib` 定义了一个包装类，定义了一个加载 MNIST 数据集的函数，对不同的最近邻变换器进行了基准测试，并可视化了 t-SNE 嵌入。我们了解到，默认的带有内部 `NearestNeighbors` 实现的 `TSNE` 估计器在性能方面大致等同于带有 `TSNE` 和 `KNeighborsTransformer` 的管道。我们还了解到，近似的 `NMSlibTransformer` 在最小的数据集上已经比精确搜索略快，但在样本数量较多的数据集上，这种速度差异预计会变得更加显著。
