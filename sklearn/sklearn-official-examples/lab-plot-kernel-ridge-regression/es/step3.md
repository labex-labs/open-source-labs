# Comparar los tiempos de SVR y regresión de Ridge Kernel

Compararemos los tiempos de ajuste y predicción de los modelos de SVR y KRR utilizando los mejores hiperparámetros encontrados en el Paso 2.

```python
import time

# Fit SVR
t0 = time.time()
svr.fit(X[:train_size], y[:train_size])
svr_fit = time.time() - t0

# Print the best params and score for SVR model
print(f"Mejor SVR con parámetros: {svr.best_params_} y puntuación R2: {svr.best_score_:.3f}")
print("Se seleccionó la complejidad y la anchura de banda de SVR y se ajustó el modelo en %.3f s" % svr_fit)

# Fit KRR
t0 = time.time()
kr.fit(X[:train_size], y[:train_size])
kr_fit = time.time() - t0

# Print the best params and score for KRR model
print(f"Mejor KRR con parámetros: {kr.best_params_} y puntuación R2: {kr.best_score_:.3f}")
print("Se seleccionó la complejidad y la anchura de banda de KRR y se ajustó el modelo en %.3f s" % kr_fit)

# Compute the support vector ratio for SVR
sv_ratio = svr.best_estimator_.support_.shape[0] / train_size
print("Ratio de vectores de soporte: %.3f" % sv_ratio)

# Predict using SVR
t0 = time.time()
y_svr = svr.predict(X_plot)
svr_predict = time.time() - t0
print("Predicción de SVR para %d entradas en %.3f s" % (X_plot.shape[0], svr_predict))

# Predict using KRR
t0 = time.time()
y_kr = kr.predict(X_plot)
kr_predict = time.time() - t0
print("Predicción de KRR para %d entradas en %.3f s" % (X_plot.shape[0], kr_predict))
```
