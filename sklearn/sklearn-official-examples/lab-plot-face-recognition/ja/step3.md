# データの前処理

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
```

データセットを訓練セットとテストセットに分割し、`StandardScaler()`関数を使用して入力データをスケーリングすることでデータを前処理します。
