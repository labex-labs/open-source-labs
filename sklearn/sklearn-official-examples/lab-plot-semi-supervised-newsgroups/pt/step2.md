# Criar o Pipeline para Aprendizagem Supervisionada

Nesta etapa, criaremos um pipeline para aprendizado supervisionado. O pipeline consistirá em um `CountVectorizer` para converter os dados de texto em uma matriz de contagens de tokens, um `TfidfTransformer` para aplicar a normalização de frequência de termo-inversa de documento à matriz de contagens e um `SGDClassifier` para treinar o modelo.

```python
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline

# Parâmetros para o SGDClassifier
sdg_params = dict(alpha=1e-5, penalty="l2", loss="log_loss")

# Parâmetros para o CountVectorizer
vectorizer_params = dict(ngram_range=(1, 2), min_df=5, max_df=0.8)

# Criar o pipeline
pipeline = Pipeline(
    [
        ("vect", CountVectorizer(**vectorizer_params)),
        ("tfidf", TfidfTransformer()),
        ("clf", SGDClassifier(**sdg_params)),
    ]
)
```
