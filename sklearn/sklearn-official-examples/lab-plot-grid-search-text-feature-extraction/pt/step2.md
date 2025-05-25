# Definir Pipeline com Ajuste de Hiperparâmetros

Definimos um pipeline que combina um vetorizador de características de texto com um classificador simples para classificação de texto. Usaremos o Complement Naive Bayes como classificador e o TfidfVectorizer para extração de características.

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import ComplementNB
from sklearn.pipeline import Pipeline
import numpy as np

pipeline = Pipeline(
    [
        ("vect", TfidfVectorizer()),
        ("clf", ComplementNB()),
    ]
)

parameter_grid = {
    "vect__max_df": (0.2, 0.4, 0.6, 0.8, 1.0),
    "vect__min_df": (1, 3, 5, 10),
    "vect__ngram_range": ((1, 1), (1, 2)),  # unigramas ou bigramas
    "vect__norm": ("l1", "l2"),
    "clf__alpha": np.logspace(-6, 6, 13),
}
```
