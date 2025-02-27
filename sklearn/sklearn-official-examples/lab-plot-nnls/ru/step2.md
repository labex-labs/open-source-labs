# Разделение данных на обучающую и тестовую выборки

Мы разделим наши данные на обучающую и тестовую выборки, при этом в каждой выборке будет по 50% данных.

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)
```
