# データを読み込んで前処理する

次に、アヤメのデータセットを読み込み、StandardScalerを使って特徴量をスケーリングすることで前処理を行います。

```python
# アヤメのデータセットを読み込む
iris = load_iris()
X, y = iris.data, iris.target

# 特徴量をスケーリングする
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# データを訓練用とテスト用に分割する
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
```
