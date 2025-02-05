# 训练管道

现在我们将使用`fit`方法在训练子集上训练管道。在训练过程中，`SelectKBest`函数将基于方差分析F值选择3个最具信息量的特征，而`LinearSVC`函数将在所选特征上训练一个线性支持向量机分类器。

```python
anova_svm.fit(X_train, y_train)
```
