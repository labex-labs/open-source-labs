# Построение простого конвейера с этапом предварительной обработки и классификатором

В этом шаге мы построим простой конвейер с этапом предварительной обработки и классификатором, и покажем его визуальное представление.

Во - первых, импортируем необходимые модули:

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn import set_config
```

Далее определяем шаги конвейера:

```python
steps = [
    ("preprocessing", StandardScaler()),
    ("classifier", LogisticRegression()),
]
```

Затем создаем конвейер:

```python
pipe = Pipeline(steps)
```

Наконец, показываем визуальное представление конвейера:

```python
set_config(display="diagram")
pipe
```
