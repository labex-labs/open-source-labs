# Construyendo una tubería simple con un paso de preprocesamiento y un clasificador

En este paso, construiremos una tubería simple con un paso de preprocesamiento y un clasificador, y mostraremos su representación visual.

Primero, importamos los módulos necesarios:

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn import set_config
```

Luego, definimos los pasos de la tubería:

```python
steps = [
    ("preprocessing", StandardScaler()),
    ("classifier", LogisticRegression()),
]
```

Después, creamos la tubería:

```python
pipe = Pipeline(steps)
```

Finalmente, mostramos la representación visual de la tubería:

```python
set_config(display="diagram")
pipe
```
