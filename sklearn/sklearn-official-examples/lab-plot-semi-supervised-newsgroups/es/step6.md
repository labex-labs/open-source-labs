# Crear el pipeline para LabelSpreading

En este paso, crearemos un pipeline para el aprendizaje semi-supervisado utilizando LabelSpreading. El pipeline será similar al pipeline supervisado, pero utilizaremos el algoritmo LabelSpreading en lugar del SGDClassifier.

```python
from sklearn.semi_supervised import LabelSpreading
from sklearn.preprocessing import FunctionTransformer

# Crear el pipeline de LabelSpreading
ls_pipeline = Pipeline(
    [
        ("vect", CountVectorizer(**vectorizer_params)),
        ("tfidf", TfidfTransformer()),
        ("toarray", FunctionTransformer(lambda x: x.toarray())),
        ("clf", LabelSpreading()),
    ]
)
```
