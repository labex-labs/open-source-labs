# Preprocesamiento de los datos de texto

Antes de poder utilizar los datos de texto para el aprendizaje automático, es necesario preprocesarlos. Esto implica varios pasos, como eliminar la puntuación, convertir todo el texto a minúsculas y tokenizar el texto en palabras individuales. Podemos realizar estos pasos de preprocesamiento utilizando `CountVectorizer` y `TfidfTransformer` de scikit-learn.

```python
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

# Preprocesa los datos de texto
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(twenty_train.data)

tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
```

Ahora nuestros datos de texto están preprocesados y listos para la extracción de características.
