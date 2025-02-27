# モデルの訓練

ここでは、トレーニングデータを使用して LOF モデルを訓練します。近傍の数を 20、新奇性検出モードを有効にし、コンタミネーション率を 0.1 に設定します。

```python
clf = LocalOutlierFactor(n_neighbors=20, novelty=True, contamination=0.1)
clf.fit(X_train)
```
