# 定义分类器

我们将定义几个用于分类的在线求解器，每个求解器都有不同的超参数。我们将使用以下分类器：

- SGDClassifier
- 感知机（Perceptron）
- 被动攻击分类器（PassiveAggressiveClassifier）
- 逻辑回归（LogisticRegression）

```python
from sklearn.linear_model import SGDClassifier, Perceptron, PassiveAggressiveClassifier, LogisticRegression

classifiers = [
    ("随机梯度下降（SGD）", SGDClassifier(max_iter=1000)),
    ("感知机", Perceptron(max_iter=1000)),
    ("被动攻击 I 型", PassiveAggressiveClassifier(max_iter=1000, loss="hinge", C=1.0, tol=1e-4)),
    ("被动攻击 II 型", PassiveAggressiveClassifier(max_iter=1000, loss="squared_hinge", C=1.0, tol=1e-4)),
    ("逻辑回归", LogisticRegression(max_iter=1000))
]
```
