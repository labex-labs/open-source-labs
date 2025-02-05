# 估计器评分方法

估计器评分方法是 scikit-learn 为每个估计器提供的默认评估标准。它计算一个代表模型预测质量的分数。你可以在每个估计器的文档中找到更多相关信息。

以下是对一个估计器使用 `score` 方法的示例：

```python
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_digits

X, y = load_digits(return_X_y=True)
clf = LogisticRegression()
clf.fit(X, y)

score = clf.score(X, y)
print("Score:", score)
```
