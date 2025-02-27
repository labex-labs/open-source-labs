# Обучение модели

Теперь мы создаем объект линейной регрессии и обучаем модель с использованием обучающих наборов данных.

```python
from sklearn import linear_model

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(diabetes_X_train, diabetes_y_train)
```
