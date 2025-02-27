# Estimatorスコアメソッド

Estimatorスコアメソッドは、scikit - learnによって各Estimatorに対して提供される既定の評価基準です。これは、モデルの予測の品質を表すスコアを計算します。各Estimatorのドキュメントでこれに関する詳細を見つけることができます。

以下は、Estimatorに対して`score`メソッドを使用する例です。

```python
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_digits

X, y = load_digits(return_X_y=True)
clf = LogisticRegression()
clf.fit(X, y)

score = clf.score(X, y)
print("Score:", score)
```
