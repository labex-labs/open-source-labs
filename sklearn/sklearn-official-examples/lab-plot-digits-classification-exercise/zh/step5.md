# 训练和测试逻辑回归分类器

现在我们将使用scikit-learn的`LogisticRegression`函数训练一个逻辑回归分类器，并在测试集上进行测试。然后我们将打印该分类器的准确率得分。

```python
from sklearn.linear_model import LogisticRegression

logistic = LogisticRegression(max_iter=1000)
logistic.fit(X_train, y_train)
logistic_score = logistic.score(X_test, y_test)

print("Logistic Regression score: %f" % logistic_score)
```
