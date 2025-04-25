# 拟合加权模型

我们使用与步骤 4 中相同的算法来拟合一个加权模型，但这次我们将 sample_weight 参数传递给 fit 方法。然后，我们绘制加权模型的决策函数。

```python
clf = linear_model.SGDClassifier(alpha=0.01, max_iter=100)
clf.fit(X, y, sample_weight=sample_weight)
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
samples_weights = ax.contour(xx, yy, Z, levels=[0], linestyles=["dashed"])
```
