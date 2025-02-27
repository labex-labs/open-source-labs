# Construyendo una tubería con reducción de dimensionalidad y clasificador

En este paso, construiremos una tubería con un paso de reducción de dimensionalidad y un clasificador, y mostraremos su representación visual.

Primero, importamos los módulos necesarios:

```python
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.decomposition import PCA
```

Luego, definimos los pasos de la tubería:

```python
steps = [("reduce_dim", PCA(n_components=4)), ("classifier", SVC(kernel="linear"))]
```

Después, creamos la tubería:

```python
pipe = Pipeline(steps)
```

Finalmente, mostramos la representación visual de la tubería:

```python
pipe
```
