# Entrenamiento del modelo

Ahora que tenemos nuestros vectores de características, podemos entrenar un modelo para clasificar los datos de texto. En este ejemplo, utilizaremos el algoritmo Multinomial Naive Bayes, que es un algoritmo popular para la clasificación de texto.

```python
from sklearn.naive_bayes import MultinomialNB

# Entrena el modelo
clf = MultinomialNB().fit(X_train_tfidf, twenty_train.target)
```

Ahora nuestro modelo está entrenado y listo para hacer predicciones.
