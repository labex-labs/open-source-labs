# ランダムフォレスト分類器 (Random Forest Classifier) の適合

次に、訓練データにランダムフォレスト分類器 (Random Forest Classifier) を適合させます。ランダムフォレスト分類器もアンサンブル法の一種で、ブートストラップサンプリングを用いて複数の決定木を作成します。ただし、各分割では特徴量の一部のみを考慮することで、さらにランダム性を加えています。

```python
random_forest = RandomForestClassifier(n_estimators=10)
random_forest.fit(X_train, y_train)
```
