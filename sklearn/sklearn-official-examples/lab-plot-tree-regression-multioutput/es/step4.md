# Predecir

En este paso, haremos predicciones utilizando los modelos que creamos en el paso anterior. Utilizaremos `np.arange` para crear una nueva matriz de valores de -100 a 100 con un intervalo de 0.01, y luego usaremos el método `predict` de nuestros modelos para predecir la salida.

```python
# Predict
X_test = np.arange(-100.0, 100.0, 0.01)[:, np.newaxis]
y_1 = regr_1.predict(X_test)
y_2 = regr_2.predict(X_test)
y_3 = regr_3.predict(X_test)
```
