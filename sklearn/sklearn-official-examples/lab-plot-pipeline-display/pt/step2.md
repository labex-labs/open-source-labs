# Construindo um Pipeline com Múltiplas Etapas de Pré-processamento e um Classificador

Neste passo, construiremos um pipeline com múltiplas etapas de pré-processamento e um classificador, e exibiremos sua representação visual.

Primeiro, importamos os módulos necessários:

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import LogisticRegression
```

Em seguida, definimos as etapas do pipeline:

```python
steps = [
    ("standard_scaler", StandardScaler()),
    ("polynomial", PolynomialFeatures(degree=3)),
    ("classifier", LogisticRegression(C=2.0)),
]
```

Então, criamos o pipeline:

```python
pipe = Pipeline(steps)
```

Finalmente, exibimos a representação visual do pipeline:

```python
pipe
```
