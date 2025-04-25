# Estimator スコアメソッド

Estimator スコアメソッドは、scikit - learn によって各 Estimator に対して提供される既定の評価基準です。これは、モデルの予測の品質を表すスコアを計算します。各 Estimator のドキュメントでこれに関する詳細を見つけることができます。

以下は、Estimator に対して`score`メソッドを使用する例です。

```python
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_digits

X, y = load_digits(return_X_y=True)
clf = LogisticRegression()
clf.fit(X, y)

score = clf.score(X, y)
print("Score:", score)
```
