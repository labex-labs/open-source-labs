# Разделение набора данных

Далее мы разделяем набор данных на обучающую и тестовую выборки. Мы будем использовать 80% данных для обучения и 20% для тестирования.

```python
# Split the data into training/testing sets
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]

# Split the targets into training/testing sets
diabetes_y_train = diabetes_y[:-20]
diabetes_y_test = diabetes_y[-20:]
```
