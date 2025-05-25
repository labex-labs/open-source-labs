# Construindo um Pipeline Simples com uma Etapa de Pré-processamento e um Classificador

Neste passo, construiremos um pipeline simples com uma etapa de pré-processamento e um classificador, e exibiremos sua representação visual.

Primeiro, importamos os módulos necessários:

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn import set_config
```

Em seguida, definimos as etapas do pipeline:

```python
steps = [
    ("preprocessing", StandardScaler()),
    ("classifier", LogisticRegression()),
]
```

Então, criamos o pipeline:

```python
pipe = Pipeline(steps)
```

Finalmente, exibimos a representação visual do pipeline:

```python
set_config(display="diagram")
pipe
```
