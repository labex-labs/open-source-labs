# Мультивыходная регрессия

#### Описание задачи

Мультивыходная регрессия предсказывает несколько числовых свойств для каждого образца. Каждое свойство является числовой переменной, и количество свойств может быть больше или равно двум.

#### Формат целевых переменных

Допустимым представлением целевых переменных для мультивыходной регрессии является плотная матрица, где каждая строка представляет собой образец, а каждый столбец - отдельное свойство.

#### Пример

Создадим задачу мультивыходной регрессии с использованием функции make_regression:

```python
from sklearn.datasets import make_regression
from sklearn.multioutput import MultiOutputRegressor
from sklearn.linear_model import LinearRegression

# Сгенерируем задачу мультивыходной регрессии
X, y = make_regression(n_samples=100, n_features=10, n_targets=3, random_state=0)

# Обучим мультивыходную линейную регрессию
model = MultiOutputRegressor(LinearRegression())
model.fit(X, y)

# Предскажем значения свойств
predictions = model.predict(X)
print(predictions)
```
