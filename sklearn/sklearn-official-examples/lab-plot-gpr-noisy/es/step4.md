# Visualización de datos

En este paso, visualizaremos el conjunto de datos de entrenamiento con ruido junto con la señal esperada.

```python
plt.plot(X, y, label="Señal esperada")
plt.scatter(
    x=X_train[:, 0],
    y=y_train,
    color="black",
    alpha=0.4,
    label="Observaciones",
)
plt.legend()
plt.xlabel("X")
_ = plt.ylabel("y")
```
