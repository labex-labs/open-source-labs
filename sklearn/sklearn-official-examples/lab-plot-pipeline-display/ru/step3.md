# Построение конвейера с уменьшением размерности и классификатором

В этом шаге мы построим конвейер с этапом уменьшения размерности и классификатором, и покажем его визуальное представление.

Во - первых, импортируем необходимые модули:

```python
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.decomposition import PCA
```

Далее определяем шаги конвейера:

```python
steps = [("reduce_dim", PCA(n_components=4)), ("classifier", SVC(kernel="linear"))]
```

Затем создаем конвейер:

```python
pipe = Pipeline(steps)
```

Наконец, показываем визуальное представление конвейера:

```python
pipe
```
