# Crear el pipeline para el aprendizaje supervisado

En este paso, crearemos un pipeline para el aprendizaje supervisado. El pipeline consistirá en un CountVectorizer para convertir los datos de texto en una matriz de conteos de tokens, un TfidfTransformer para aplicar la normalización de frecuencia de término-inversa de frecuencia de documento a la matriz de conteos y un SGDClassifier para entrenar el modelo.

```python
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline

# Parámetros para el SGDClassifier
sdg_params = dict(alpha=1e-5, penalty="l2", loss="log_loss")

# Parámetros para el CountVectorizer
vectorizer_params = dict(ngram_range=(1, 2), min_df=5, max_df=0.8)

# Crear el pipeline
pipeline = Pipeline(
    [
        ("vect", CountVectorizer(**vectorizer_params)),
        ("tfidf", TfidfTransformer()),
        ("clf", SGDClassifier(**sdg_params)),
    ]
)
```
