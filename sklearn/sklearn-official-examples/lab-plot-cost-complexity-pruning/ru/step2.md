# Разделение данных

Мы разделим данные на обучающий набор и тестовый набор.

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
```
