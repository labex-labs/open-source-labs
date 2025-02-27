# データセットを学習用とテスト用に分割する

モデルの性能を評価するために、データセットを学習用とテスト用に分割する必要があります。これを行うには、scikit - learnライブラリの`train_test_split`関数を使用します。

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)
```
