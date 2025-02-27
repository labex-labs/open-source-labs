# 重み付きモデルをフィットさせる

ステップ4と同じアルゴリズムを使って重み付きモデルをフィットさせますが、今回はサンプル重み（sample_weight）引数をfitメソッドに渡します。その後、重み付きモデルの決定関数をプロットします。

```python
clf = linear_model.SGDClassifier(alpha=0.01, max_iter=100)
clf.fit(X, y, sample_weight=sample_weight)
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
samples_weights = ax.contour(xx, yy, Z, levels=[0], linestyles=["dashed"])
```
