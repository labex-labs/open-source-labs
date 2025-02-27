# Definiere Pipeline mit Hyperparameteroptimierung

Wir definieren eine Pipeline, die einen Text-Feature-Vektorizer mit einem einfachen Klassifikator für die Textklassifikation kombiniert. Wir werden Complement Naive Bayes als Klassifikator und TfidfVectorizer zur Feature-Extraktion verwenden.

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