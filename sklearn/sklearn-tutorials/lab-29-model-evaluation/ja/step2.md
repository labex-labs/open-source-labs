# 評価パラメータ

scikit - learn は、交差検証やグリッドサーチなどのいくつかのモデル評価ツールに`scoring`パラメータを提供しています。`scoring`パラメータは、評価中に Estimator に適用されるメトリックを制御します。

以下は、交差検証で`scoring`パラメータを使用する例です。

```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_digits

X, y = load_digits(return_X_y=True)
clf = LogisticRegression()

scores = cross_val_score(clf, X, y, cv=5, scoring='accuracy')
print("Scores:", scores)
```
