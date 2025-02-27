# Configurar el vectorizador y reservar un conjunto de prueba

```python
# Crear el vectorizador y limitar el número de características a un máximo razonable
vectorizer = HashingVectorizer(decode_error="ignore", n_features=2**18, alternate_sign=False)

# Iterador sobre los archivos SGML de Reuters analizados.
data_stream = stream_reuters_documents()

# Aprendemos una clasificación binaria entre la clase "acq" y todas las demás.
# "acq" fue elegido porque está más o menos equitativamente distribuida en los archivos de Reuters.
# Para otros conjuntos de datos, se debe tener cuidado de crear un conjunto de prueba con una proporción realista de instancias positivas.
all_classes = np.array([0, 1])
positive_class = "acq"

# Aquí hay algunos clasificadores que admiten el método `partial_fit`
partial_fit_classifiers = {
    "SGD": SGDClassifier(max_iter=5),
    "Perceptron": Perceptron(),
    "NB Multinomial": MultinomialNB(alpha=0.01),
    "Passive-Aggressive": PassiveAggressiveClassifier(),
}

# Estadísticas de los datos de prueba
test_stats = {"n_test": 0, "n_test_pos": 0}

# Primero, reservamos un número de ejemplos para estimar la precisión
n_test_documents = 1000
X_test_text, y_test = get_minibatch(data_stream, 1000)
X_test = vectorizer.transform(X_test_text)
test_stats["n_test"] += len(y_test)
test_stats["n_test_pos"] += sum(y_test)
print("El conjunto de prueba es %d documentos (%d positivos)" % (len(y_test), sum(y_test)))
```
