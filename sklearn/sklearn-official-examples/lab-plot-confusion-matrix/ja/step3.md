# データの分割

データセットを訓練セットとテストセットに分割します。訓練セットはモデルの訓練に使用され、テストセットはモデルの性能評価に使用されます。

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
```
