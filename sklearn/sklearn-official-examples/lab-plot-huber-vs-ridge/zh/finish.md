# 总结

在本实验中，我们在一个包含强异常值的数据集上比较了两种回归模型——HuberRegressor 和 Ridge 的性能。我们生成了一个简单的数据集，向其中添加了强异常值，然后将这两种模型都拟合到该数据集上。我们对结果进行了可视化，并比较了模型的性能。我们观察到，HuberRegressor 比 Ridge 回归器受异常值的影响更小，并且随着 epsilon 值的增加，HuberRegressor 的决策函数趋近于 Ridge 回归器的决策函数。
