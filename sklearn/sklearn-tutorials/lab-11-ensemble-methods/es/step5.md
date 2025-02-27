# Evaluar el clasificador de ensamble (Bagging)

Evaluemos el clasificador de ensamble (Bagging) calculando la puntuación de precisión en los datos de prueba utilizando el método `score`.

```python
accuracy = bagging.score(X_test, y_test)
print(f"Precisión del clasificador de ensamble (Bagging): {accuracy}")
```
