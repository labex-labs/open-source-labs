# Créer le pipeline pour la diffusion d'étiquettes

Dans cette étape, nous allons créer un pipeline pour l'apprentissage semi-supervisé utilisant la diffusion d'étiquettes. Le pipeline sera similaire au pipeline supervisé, mais nous utiliserons l'algorithme de diffusion d'étiquettes au lieu du SGDClassifier.

```python
from sklearn.semi_supervised import LabelSpreading
from sklearn.preprocessing import FunctionTransformer

# Créer le pipeline de diffusion d'étiquettes
ls_pipeline = Pipeline(
    [
        ("vect", CountVectorizer(**vectorizer_params)),
        ("tfidf", TfidfTransformer()),
        ("toarray", FunctionTransformer(lambda x: x.toarray())),
        ("clf", LabelSpreading()),
    ]
)
```
