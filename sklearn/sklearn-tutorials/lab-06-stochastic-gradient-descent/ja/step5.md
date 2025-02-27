# 分類器の訓練

これで、scikit-learn の `SGDClassifier` クラスを使用して SGD 分類器を作成し、訓練することができます。線形分類器で一般的に使用される「ヒンジ（hinge）」損失関数を使用します。

```python
clf = SGDClassifier(loss='hinge', random_state=42)
clf.fit(X_train, y_train)
```
