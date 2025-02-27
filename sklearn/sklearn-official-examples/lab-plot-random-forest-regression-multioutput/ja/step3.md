# データを学習用とテスト用に分割する

scikit-learnの`train_test_split`関数を使って、データを400の学習用セットと200のテスト用セットに分割します。

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=400, test_size=200, random_state=4)
```
