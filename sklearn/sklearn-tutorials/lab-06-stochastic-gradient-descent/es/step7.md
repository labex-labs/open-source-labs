# Evaluar el rendimiento

Finalmente, evaluaremos el rendimiento del clasificador calculando la precisión de sus predicciones en el conjunto de prueba.

```python
accuracy = accuracy_score(y_test, y_pred)
print("Precisión:", accuracy)
```
