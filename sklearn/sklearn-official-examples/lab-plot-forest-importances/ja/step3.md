# ランダムフォレストの適合

特徴量の重要度を計算するために、ランダムフォレスト分類器を適合させます。

```python
feature_names = [f"feature {i}" for i in range(X.shape[1])]
forest = RandomForestClassifier(random_state=0)
forest.fit(X_train, y_train)
```
