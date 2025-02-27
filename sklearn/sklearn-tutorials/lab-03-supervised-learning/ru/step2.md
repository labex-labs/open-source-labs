# Линейная регрессия

В этом разделе мы изучим концепцию линейной регрессии и узнаем, как ее реализовать с использованием scikit-learn. Мы будем использовать датасет о диабете, который содержит физиологические переменные пациентов и их прогрессию заболевания спустя год.

#### Загрузка датасета о диабете

```python
diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]
diabetes_y_train = diabetes_y[:-20]
diabetes_y_test = diabetes_y[-20:]
```

#### Создание и обучение модели линейной регрессии

```python
from sklearn import linear_model

regr = linear_model.LinearRegression()
regr.fit(diabetes_X_train, diabetes_y_train)
```

#### Предсказание и расчет метрик качества

```python
predictions = regr.predict(diabetes_X_test)
mse = np.mean((predictions - diabetes_y_test)**2)
variance_score = regr.score(diabetes_X_test, diabetes_y_test)
```
