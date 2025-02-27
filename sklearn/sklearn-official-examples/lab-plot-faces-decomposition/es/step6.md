# Aprendizaje del diccionario

El aprendizaje del diccionario es un método para encontrar una representación esparsa de los datos de entrada como una combinación de elementos simples, que forman un diccionario. Aplicamos MiniBatchDictionaryLearning, que es una versión más rápida de DictionaryLearning que es más adecuada para conjuntos de datos grandes.

```python
# Aprendizaje del diccionario
batch_dict_estimator = decomposition.MiniBatchDictionaryLearning(
    n_components=n_components, alpha=0.1, max_iter=50, batch_size=3, random_state=rng
)
batch_dict_estimator.fit(faces_centered)
plot_gallery("Aprendizaje del diccionario", batch_dict_estimator.components_[:n_components])
```
