# Realizar regresión en secuencias

Podemos utilizar nuestro `SequenceKernel` para realizar regresión en secuencias. Utilizaremos un conjunto de datos de 6 secuencias y usaremos las 1ª, 2ª, 4ª y 5ª secuencias como conjunto de entrenamiento para hacer predicciones sobre las 3ª y 6ª secuencias.

```python
X = np.array(["AGCT", "AGC", "AACT", "TAA", "AAA", "GAACA"])
Y = np.array([1.0, 1.0, 2.0, 2.0, 3.0, 3.0])

training_idx = [0, 1, 3, 4]
gp = GaussianProcessRegressor(kernel=kernel)
gp.fit(X[training_idx], Y[training_idx])

plt.figure(figsize=(8, 5))
plt.bar(np.arange(len(X)), gp.predict(X), color="b", label="predicción")
plt.bar(training_idx, Y[training_idx], width=0.2, color="r", alpha=1, label="entrenamiento")
plt.xticks(np.arange(len(X)), X)
plt.title("Regresión en secuencias")
plt.legend()
plt.show()
```
