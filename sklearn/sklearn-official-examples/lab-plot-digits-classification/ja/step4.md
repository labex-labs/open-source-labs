# データセットを分割する

`sklearn.model_selection` の `train_test_split()` メソッドを使用して、データセットを 50% の学習用と 50% のテスト用のサブセットに分割します。

```python
X_train, X_test, y_train, y_test = train_test_split(
    data, digits.target, test_size=0.5, shuffle=False
)
```
