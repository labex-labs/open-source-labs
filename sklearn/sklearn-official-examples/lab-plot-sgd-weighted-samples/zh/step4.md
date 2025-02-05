# 拟合未加权模型

我们使用scikit-learn库中的SGDClassifier算法拟合一个未加权模型。然后，我们绘制未加权模型的决策函数。

```python
clf = linear_model.SGDClassifier(alpha=0.01, max_iter=100)
clf.fit(X, y)
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
no_weights = ax.contour(xx, yy, Z, levels=[0], linestyles=["solid"])
```
