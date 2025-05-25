# 분류기 정의

다양한 하이퍼파라미터를 가진 여러 온라인 분류 솔버를 정의합니다. 다음 분류기를 사용합니다.

- SGDClassifier
- Perceptron
- PassiveAggressiveClassifier
- LogisticRegression

```python
from sklearn.linear_model import SGDClassifier, Perceptron, PassiveAggressiveClassifier, LogisticRegression

classifiers = [
    ("SGD", SGDClassifier(max_iter=1000)),
    ("Perceptron", Perceptron(max_iter=1000)),
    ("Passive-Aggressive I", PassiveAggressiveClassifier(max_iter=1000, loss="hinge", C=1.0, tol=1e-4)),
    ("Passive-Aggressive II", PassiveAggressiveClassifier(max_iter=1000, loss="squared_hinge", C=1.0, tol=1e-4)),
    ("LogisticRegression", LogisticRegression(max_iter=1000))
]
```
