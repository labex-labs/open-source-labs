# Créer le pipeline pour l'auto-apprentissage

Dans cette étape, nous allons créer un pipeline pour l'apprentissage semi-supervisé utilisant l'auto-apprentissage. Le pipeline sera similaire au pipeline supervisé, mais nous utiliserons le SelfTrainingClassifier au lieu du SGDClassifier.

```python
from sklearn.semi_supervised import SelfTrainingClassifier

# Créer le pipeline d'auto-apprentissage
st_pipeline = Pipeline(
    [
        ("vect", CountVectorizer(**vectorizer_params)),
        ("tfidf", TfidfTransformer()),
        ("clf", SelfTrainingClassifier(SGDClassifier(**sdg_params), verbose=True)),
    ]
)
```
