# Trazar la curva ROC

A continuación, trazaremos la curva ROC utilizando la función `RocCurveDisplay.from_estimator`. Esta función toma el clasificador entrenado, el conjunto de datos de prueba y las etiquetas verdaderas como entradas, y devuelve un objeto que se puede utilizar para trazar la curva ROC. Luego llamaremos al método `show()` para mostrar la gráfica.

```python
svc_disp = RocCurveDisplay.from_estimator(svc, X_test, y_test)
svc_disp.show()
```
