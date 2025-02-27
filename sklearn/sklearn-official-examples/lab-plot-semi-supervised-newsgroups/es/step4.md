# Crear el pipeline para el Autoentrenamiento

En este paso, crearemos un pipeline para el aprendizaje semi-supervisado utilizando el Autoentrenamiento. El pipeline será similar al pipeline supervisado, pero utilizaremos el SelfTrainingClassifier en lugar del SGDClassifier.

```python
from sklearn.semi_supervised import SelfTrainingClassifier

# Crear el pipeline de Autoentrenamiento
st_pipeline = Pipeline(
    [
        ("vect", CountVectorizer(**vectorizer_params)),
        ("tfidf", TfidfTransformer()),
        ("clf", SelfTrainingClassifier(SGDClassifier(**sdg_params), verbose=True)),
    ]
)
```
