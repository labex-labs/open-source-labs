# Créer le pipeline pour l'apprentissage supervisé

Dans cette étape, nous allons créer un pipeline pour l'apprentissage supervisé. Le pipeline comprendra un CountVectorizer pour convertir les données textuelles en une matrice de comptes de jetons, un TfidfTransformer pour appliquer la normalisation fréquence de terme - fréquence inverse de document à la matrice de comptes, et un SGDClassifier pour entraîner le modèle.

```python
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline

# Paramètres pour le SGDClassifier
sdg_params = dict(alpha=1e-5, penalty="l2", loss="log_loss")

# Paramètres pour le CountVectorizer
vectorizer_params = dict(ngram_range=(1, 2), min_df=5, max_df=0.8)

# Créer le pipeline
pipeline = Pipeline(
    [
        ("vect", CountVectorizer(**vectorizer_params)),
        ("tfidf", TfidfTransformer()),
        ("clf", SGDClassifier(**sdg_params)),
    ]
)
```
