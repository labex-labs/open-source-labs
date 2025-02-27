# Выбор признаков с использованием SelectFromModel

Класс `SelectFromModel` - это мета-трансформер, который можно использовать с любым оценивателем, который назначает важность каждому признаку. Он выбирает признаки на основе их важности и удаляет признаки, значения которых ниже заданного порога.

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectFromModel

# Load the Iris dataset
X, y = load_iris(return_X_y=True)

# Initialize RandomForestClassifier as the estimator
estimator = RandomForestClassifier()

# Initialize SelectFromModel with the estimator and threshold of "mean"
selector = SelectFromModel(estimator, threshold="mean")

# Select the best features
X_selected = selector.fit_transform(X, y)

print("Original X shape:", X.shape)
print("X with selected features shape:", X_selected.shape)
print("Selected features:", selector.get_support(indices=True))
```

В этом примере мы используем классификатор случайного леса в качестве оценивателя и выбираем признаки с важностью выше средней важности. Вывод покажет исходную форму набора данных и форму после выбора наилучших признаков.
