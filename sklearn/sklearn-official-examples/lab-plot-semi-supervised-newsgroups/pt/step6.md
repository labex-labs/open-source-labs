# Criar o Pipeline para Propagação de Rótulos

Nesta etapa, criaremos um pipeline para aprendizado semi-supervisionado usando a técnica de Propagação de Rótulos (LabelSpreading). O pipeline será semelhante ao pipeline supervisionado, mas usaremos o algoritmo `LabelSpreading` em vez do `SGDClassifier`.

```python
from sklearn.semi_supervised import LabelSpreading
from sklearn.preprocessing import FunctionTransformer

# Criar o pipeline de Propagação de Rótulos
ls_pipeline = Pipeline(
    [
        ("vect", CountVectorizer(**vectorizer_params)),
        ("tfidf", TfidfTransformer()),
        ("toarray", FunctionTransformer(lambda x: x.toarray())),
        ("clf", LabelSpreading()),
    ]
)
```
