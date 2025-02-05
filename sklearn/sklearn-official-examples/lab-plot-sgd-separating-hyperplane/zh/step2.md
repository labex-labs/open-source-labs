# 使用随机梯度下降训练支持向量机模型

接下来，我们需要使用随机梯度下降来训练支持向量机模型。我们将使用Scikit-learn中的`SGDClassifier`类来训练模型。我们将把`loss`参数设置为“hinge”以使用支持向量机算法，并将`alpha`参数设置为0.01来控制正则化强度。我们还将把`max_iter`参数设置为200以限制迭代次数。

```python
# 拟合模型
clf = SGDClassifier(loss="hinge", alpha=0.01, max_iter=200)
clf.fit(X, Y)
```
