# 重みなしモデルをフィットさせる

scikit-learnライブラリのSGDClassifierアルゴリズムを使って重みなしモデルをフィットさせます。その後、重みなしモデルの決定関数をプロットします。

```python
clf = linear_model.SGDClassifier(alpha=0.01, max_iter=100)
clf.fit(X, y)
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
no_weights = ax.contour(xx, yy, Z, levels=[0], linestyles=["solid"])
```
