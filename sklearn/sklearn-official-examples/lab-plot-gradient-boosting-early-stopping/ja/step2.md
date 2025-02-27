# データの準備

次に、データを訓練セットとテストセットに分割することでデータを準備します。

```python
for X, y in data_list:
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=0
    )
```
