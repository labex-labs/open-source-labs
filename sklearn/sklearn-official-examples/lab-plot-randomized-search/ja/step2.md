# SVM モデルを作成する

確率的勾配降下法（SGD）を用いて線形 SVM モデルを作成します。

```python
# create SVM model with SGD training
clf = SGDClassifier(loss="hinge", penalty="elasticnet", fit_intercept=True)
```
