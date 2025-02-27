# Construyendo una tubería con encadenamiento de múltiples pasos de preprocesamiento y un clasificador

En este paso, construiremos una tubería con múltiples pasos de preprocesamiento y un clasificador, y mostraremos su representación visual.

Primero, importamos los módulos necesarios:

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import LogisticRegression
```

Luego, definimos los pasos de la tubería:

```python
steps = [
    ("standard_scaler", StandardScaler()),
    ("polynomial", PolynomialFeatures(degree=3)),
    ("classifier", LogisticRegression(C=2.0)),
]
```

Después, creamos la tubería:

```python
pipe = Pipeline(steps)
```

Finalmente, mostramos la representación visual de la tubería:

```python
pipe
```
