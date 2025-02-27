# Predicciones e intervalos de confianza

Después de ajustar nuestro modelo, vemos que los hiperparámetros del kernel han sido optimizados. Ahora, usaremos nuestro kernel para calcular la predicción media del conjunto de datos completo y graficar el intervalo de confianza del 95%.

```python
mean_prediction, std_prediction = gaussian_process.predict(X, return_std=True)

plt.plot(X, y, label=r"$f(x) = x \sin(x)$", linestyle="dotted")
plt.scatter(X_train, y_train, label="Observaciones")
plt.plot(X, mean_prediction, label="Predicción media")
plt.fill_between(
    X.ravel(),
    mean_prediction - 1.96 * std_prediction,
    mean_prediction + 1.96 * std_prediction,
    alpha=0.5,
    label=r"Intervalo de confianza del 95%",
)
plt.legend()
plt.xlabel("$x$")
plt.ylabel("$f(x)$")
_ = plt.title("Regresión con procesos gaussianos en conjunto de datos sin ruido")
```
