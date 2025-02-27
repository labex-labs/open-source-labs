# Evaluación del modelo

Para evaluar el rendimiento de nuestro modelo, podemos utilizar un conjunto de prueba separado. Podemos cargar el conjunto de prueba utilizando el mismo proceso que el conjunto de entrenamiento.

```python
twenty_test = fetch_20newsgroups(subset='test', categories=categories, shuffle=True, random_state=42)
```

Ahora podemos preprocesar el conjunto de prueba y extraer los vectores de características.

```python
X_test_counts = count_vect.transform(twenty_test.data)
X_test_tfidf = tfidf_transformer.transform(X_test_counts)
```

Finalmente, podemos utilizar nuestro modelo entrenado para hacer predicciones en el conjunto de prueba y calcular la precisión.

```python
predicted = clf.predict(X_test_tfidf)
accuracy = np.mean(predicted == twenty_test.target)
```
