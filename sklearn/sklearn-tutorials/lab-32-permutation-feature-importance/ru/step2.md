# Обучение модели

Далее мы обучим регрессионную модель на тренировочных данных. В этом примере мы будем использовать модель Ridge - регрессии.

```python
from sklearn.linear_model import Ridge

# Train the Ridge regression model
модель = Ridge(alpha = 1e - 2).fit(X_train, y_train)
```
