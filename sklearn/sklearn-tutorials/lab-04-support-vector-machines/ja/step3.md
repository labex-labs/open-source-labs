# スコアと確率

- SVM は直接確率推定を提供しませんが、`probability` パラメータを `True` に設定することで確率推定を有効にすることができます：

```python
clf = svm.SVC(probability=True)
clf.fit(X, y)
```

- その後、`predict_proba` メソッドを使って各クラスの確率を取得することができます：

```python
clf.predict_proba([[2., 2.]])
```

- 確率推定はコストがかかり、クロスバリデーションが必要ですので、慎重に使用してください。
