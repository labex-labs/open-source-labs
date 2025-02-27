# Построение конвейера, объединяющего несколько этапов предварительной обработки и классификатор

В этом шаге мы построим конвейер с несколькими этапами предварительной обработки и классификатором, и покажем его визуальное представление.

Во - первых, импортируем необходимые модули:

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import LogisticRegression
```

Далее определяем шаги конвейера:

```python
steps = [
    ("standard_scaler", StandardScaler()),
    ("polynomial", PolynomialFeatures(degree=3)),
    ("classifier", LogisticRegression(C=2.0)),
]
```

Затем создаем конвейер:

```python
pipe = Pipeline(steps)
```

Наконец, показываем визуальное представление конвейера:

```python
pipe
```
