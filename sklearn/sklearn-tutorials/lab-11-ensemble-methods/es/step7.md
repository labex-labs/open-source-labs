# Evaluar el clasificador de bosque aleatorio

Evaluemos el clasificador de bosque aleatorio calculando la puntuación de precisión en los datos de prueba.

```python
accuracy = random_forest.score(X_test, y_test)
print(f"Precisión del clasificador de bosque aleatorio: {accuracy}")
```
