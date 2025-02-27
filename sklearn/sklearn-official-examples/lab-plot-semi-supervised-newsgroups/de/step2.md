# Erstelle die Pipeline für das überwachte Lernen

In diesem Schritt werden wir eine Pipeline für das überwachte Lernen erstellen. Die Pipeline wird aus einem CountVectorizer bestehen, um die Textdaten in eine Matrix von Token-Zählungen umzuwandeln, einem TfidfTransformer, um die Termfrequenz-Inverse-Dokumentfrequenz-Normalisierung auf die Zählmatrix anzuwenden, und einem SGDClassifier, um das Modell zu trainieren.

```python
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline

# Parameter für den SGDClassifier
sdg_params = dict(alpha=1e-5, penalty="l2", loss="log_loss")

# Parameter für den CountVectorizer
vectorizer_params = dict(ngram_range=(1, 2), min_df=5, max_df=0.8)

# Erstelle die Pipeline
pipeline = Pipeline(
    [
        ("vect", CountVectorizer(**vectorizer_params)),
        ("tfidf", TfidfTransformer()),
        ("clf", SGDClassifier(**sdg_params)),
    ]
)
```