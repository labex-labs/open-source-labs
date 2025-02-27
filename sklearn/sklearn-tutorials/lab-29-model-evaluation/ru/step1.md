# Метод оценки Estimator

Метод оценки Estimator - это стандартный критерий оценки, предоставляемый scikit-learn для каждого оценщика. Он вычисляет оценку, представляющую качество предсказаний модели. Вы можете найти дополнительную информацию об этом в документации по каждому оценщику.

Вот пример использования метода `score` для оценщика:

```python
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_digits

X, y = load_digits(return_X_y=True)
clf = LogisticRegression()
clf.fit(X, y)

score = clf.score(X, y)
print("Score:", score)
```
