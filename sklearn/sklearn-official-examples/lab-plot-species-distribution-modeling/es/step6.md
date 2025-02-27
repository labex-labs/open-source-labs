# Predecir la distribución de especies

En este paso, predeciríamos la distribución de especies utilizando el modelo OneClassSVM. Predeciríamos la distribución de especies utilizando los datos de entrenamiento y graficaríamos los resultados.

```python
# Predecir la distribución de especies utilizando los datos de entrenamiento
Z = np.ones((data.Ny, data.Nx), dtype=np.float64)

# Solo predeciríamos para los puntos de tierra.
idx = np.where(data.coverages[6] > -9999)
coverages_land = data.coverages[:, idx[0], idx[1]].T

pred = clf.decision_function((coverages_land - mean) / std)
Z *= pred.min()
Z[idx[0], idx[1]] = pred

levels = np.linspace(Z.min(), Z.max(), 25)
Z[data.coverages[6] == -9999] = -9999

# graficar los contornos de la predicción
plt.contourf(X, Y, Z, levels=levels, cmap=plt.cm.Reds)
plt.colorbar(format="%.2f")

# dispersar los puntos de entrenamiento/prueba
plt.scatter(
    BV_bunch.pts_train["dd long"],
    BV_bunch.pts_train["dd lat"],
    s=2**2,
    c="black",
    marker="^",
    label="train",
)
plt.scatter(
    BV_bunch.pts_test["dd long"],
    BV_bunch.pts_test["dd lat"],
    s=2**2,
    c="black",
    marker="x",
    label="test",
)
plt.legend()
plt.title(BV_bunch.name)
plt.axis("equal")
```
