# データを学習用とテスト用に分割する

scikit-learn の`train_test_split`関数を使って、データを 400 の学習用セットと 200 のテスト用セットに分割します。

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=400, test_size=200, random_state=4)
```
