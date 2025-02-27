# ロジスティック回帰分類器を学習とテストする

ここでは、scikit-learnの`LogisticRegression`関数を使ってロジスティック回帰分類器を学習し、テストセットでテストします。その後、分類器の精度スコアを表示します。

```python
from sklearn.linear_model import LogisticRegression

logistic = LogisticRegression(max_iter=1000)
logistic.fit(X_train, y_train)
logistic_score = logistic.score(X_test, y_test)

print("Logistic Regression score: %f" % logistic_score)
```
