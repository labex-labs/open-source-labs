# Разделим датасет на тренировочный и тестовый наборы

Далее мы разделим датасет на тренировочный и тестовые наборы с использованием функции `train_test_split` из модуля `sklearn.model_selection`. Тренировочный набор будет использоваться для обучения наивного байесовского классификатора, а тестовый набор - для оценки его производительности.

```python
from sklearn.model_selection import train_test_split

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```
