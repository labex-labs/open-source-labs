# モデルの訓練

ここでは、fit()メソッドを使ってアイリスデータセット上でSGDClassifierモデルを訓練します。このメソッドは、入力データとターゲット値を入力として受け取り、与えられたデータでモデルを訓練します。

```python
clf = SGDClassifier(alpha=0.001, max_iter=100).fit(X, y)
```
