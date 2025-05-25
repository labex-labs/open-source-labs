# Criar o Pipeline para Autoaprendizagem

Nesta etapa, criaremos um pipeline para aprendizado semi-supervisionado usando Autoaprendizagem (Self-Training). O pipeline será semelhante ao pipeline supervisionado, mas usaremos o `SelfTrainingClassifier` em vez do `SGDClassifier`.

```python
from sklearn.semi_supervised import SelfTrainingClassifier

# Criar o pipeline de Autoaprendizagem
st_pipeline = Pipeline(
    [
        ("vect", CountVectorizer(**vectorizer_params)),
        ("tfidf", TfidfTransformer()),
        ("clf", SelfTrainingClassifier(SGDClassifier(**sdg_params), verbose=True)),
    ]
)
```
