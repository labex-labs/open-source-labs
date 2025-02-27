# すべての分類器に対するクラス確率の予測

predict_proba()関数を使用して、すべての分類器に対するクラス確率を予測します。

```python
probas = [c.fit(X, y).predict_proba(X) for c in (clf1, clf2, clf3, eclf)]
```
