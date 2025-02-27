# Параметр scoring

Scikit-learn предоставляет параметр `scoring` в нескольких инструментах оценки модели, таких как кросс-валидация и поиск по сетке. Параметр `scoring` контролирует метрику, применяемую к оценщикам в ходе оценки.

Вот пример использования параметра `scoring` с кросс-валидацией:

```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_digits

X, y = load_digits(return_X_y=True)
clf = LogisticRegression()

scores = cross_val_score(clf, X, y, cv=5, scoring='accuracy')
print("Scores:", scores)
```
