# Ordinary Least Squares

> Начните с [Supervised Learning: Regression](https://labex.io/courses/supervised-learning-regression), если у вас нет опыта в машинном обучении.

Ordinary Least Squares (OLS) - это метод линейной регрессии, который минимизирует сумму квадратов разностей между наблюдаемыми целевыми переменными и предсказанными целевыми переменными. Математически, он решает задачу вида:
$$\min_{w} || X w - y||_2^2$$

Попробуем обучить модель линейной регрессии с использованием OLS.

```python
from sklearn import linear_model

reg = linear_model.LinearRegression()
X = [[0, 0], [1, 1], [2, 2]]
y = [0, 1, 2]
reg.fit(X, y)

print(reg.coef_)
```

- Мы импортируем модуль `linear_model` из scikit-learn.
- Создаем экземпляр `LinearRegression`.
- Используем метод `fit`, чтобы обучить модель на тренировочных данных.
- Выводим коэффициенты линейной модели.
