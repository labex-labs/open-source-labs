# データ前処理

次に、データセットを分割して、学習に 90％を使用し、残りをテストに残します。また、回帰モデルのパラメータを設定します。

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=13)

params = {
    "n_estimators": 500,
    "max_depth": 4,
    "min_samples_split": 5,
    "learning_rate": 0.01,
    "loss": "squared_error",
}
```
