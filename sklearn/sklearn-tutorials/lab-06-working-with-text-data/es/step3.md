# Extracción de características

Para representar los datos de texto como vectores de características, podemos utilizar la representación de bolsas de palabras. Esta representación asigna un id entero fijo a cada palabra en el conjunto de entrenamiento y cuenta el número de ocurrencias de cada palabra en cada documento. Podemos extraer estos vectores de características utilizando `CountVectorizer` de scikit-learn.

```python
from sklearn.feature_extraction.text import CountVectorizer

# Extrae vectores de características
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(twenty_train.data)
```

Ahora hemos extraído los vectores de características y podemos utilizarlos para entrenar nuestro modelo.
