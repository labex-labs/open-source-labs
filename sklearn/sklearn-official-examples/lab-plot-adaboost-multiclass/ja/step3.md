# データセットを分割する

データセットを訓練用とテスト用に分割します。最初の3000サンプルを訓練に、残りのサンプルをテストに使用します。

```python
n_split = 3000
X_train, X_test = X[:n_split], X[n_split:]
y_train, y_test = y[:n_split], y[n_split:]
```
