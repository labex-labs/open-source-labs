# データを分割する

このステップでは、`train_test_split` を使ってデータを訓練用とテスト用のセットに分割します。

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
```
