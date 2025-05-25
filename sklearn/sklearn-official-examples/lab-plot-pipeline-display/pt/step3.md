# Construindo um Pipeline com Redução de Dimensionalidade e Classificador

Neste passo, construiremos um pipeline com uma etapa de redução de dimensionalidade e um classificador, e exibiremos sua representação visual.

Primeiro, importamos os módulos necessários:

```python
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.decomposition import PCA
```

Em seguida, definimos as etapas do pipeline:

```python
steps = [("reduce_dim", PCA(n_components=4)), ("classifier", SVC(kernel="linear"))]
```

Então, criamos o pipeline:

```python
pipe = Pipeline(steps)
```

Finalmente, exibimos a representação visual do pipeline:

```python
pipe
```
