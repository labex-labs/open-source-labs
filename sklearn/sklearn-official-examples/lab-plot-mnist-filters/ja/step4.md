# データの分割

`train_test_split` 関数を使用して、データセットを訓練データセットとテストデータセットに分割します。

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0, test_size=0.7)
```
