# Crear y entrenar el modelo MLP

```python
# Crear un clasificador MLP con una capa oculta de 5 neuronas
clf = MLPClassifier(hidden_layer_sizes=(5,), random_state=1)

# Entrenar el modelo utilizando los datos de entrenamiento
clf.fit(X, y)
```
