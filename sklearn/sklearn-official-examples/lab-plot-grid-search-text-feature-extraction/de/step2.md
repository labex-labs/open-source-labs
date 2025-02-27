# Definition einer Pipeline (Bearbeitungsreihenfolge) mit Hyperparameter-Tuning

Wir definieren eine Pipeline, die einen Textmerkmal-Vektorisierer (text feature vectorizer) mit einem einfachen Klassifikator für die Textklassifizierung kombiniert. Wir werden Complement Naive Bayes als Klassifikator und TfidfVectorizer zur Merkmalsextraktion verwenden.

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
