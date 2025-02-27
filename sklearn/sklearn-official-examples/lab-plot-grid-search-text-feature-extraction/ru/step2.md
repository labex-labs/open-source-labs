# Определение конвейера (pipeline) с настройкой гиперпараметров

Мы определяем конвейер (pipeline), который объединяет векторизатор текстовых признаков с простым классификатором для классификации текстов. Мы будем использовать Complement Naive Bayes в качестве классификатора и TfidfVectorizer для извлечения признаков.

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
    "vect__ngram_range": ((1, 1), (1, 2)),  # unigrams or bigrams
    "vect__norm": ("l1", "l2"),
    "clf__alpha": np.logspace(-6, 6, 13),
}

```
