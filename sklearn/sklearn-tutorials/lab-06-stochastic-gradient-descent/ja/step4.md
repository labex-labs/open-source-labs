# データの分割

データセットを訓練セット（training set）とテストセット（test set）に分割します。訓練セットは SGD 分類器を訓練するために使用され、テストセットはその性能を評価するために使用されます。

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```
