# 总结

在本实验中，我们学习了如何使用 Scikit-Learn 的`IterativeImputer`类来填充数据集中的缺失值。我们使用`SimpleImputer`通过均值和中位数插补比较了不同的插补策略，并使用`IterativeImputer`结合不同的估计器进行了比较。我们发现，对于加利福尼亚住房数据集中这种特定的缺失值模式，`BayesianRidge`和`RandomForestRegressor`给出了最佳结果。
