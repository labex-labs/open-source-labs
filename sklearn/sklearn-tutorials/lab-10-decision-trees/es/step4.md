# Crear y entrenar el clasificador de Árboles de Decisión

Ahora, podemos crear y entrenar el clasificador de Árboles de Decisión usando los datos de entrenamiento.

```python
# Crear un clasificador de Árboles de Decisión
clf = tree.DecisionTreeClassifier()

# Entrenar el clasificador
clf.fit(X_train, y_train)
```
