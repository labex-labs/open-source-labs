# Graficar los límites de decisión y los puntos de entrenamiento

En este paso, graficaremos los límites de decisión y los puntos de entrenamiento. Crearemos un objeto `DecisionBoundaryDisplay` utilizando el método `from_estimator` del módulo `sklearn.inspection` y pasaremos el clasificador AdaBoost, el conjunto de datos y otros parámetros. También graficaremos los puntos de entrenamiento utilizando diferentes colores para cada clase.

```python
plot_colors = "br"
plot_step = 0.02
class_names = "AB"

plt.figure(figsize=(10, 5))

# Graficar los límites de decisión
ax = plt.subplot(121)
disp = DecisionBoundaryDisplay.from_estimator(
    bdt,
    X,
    cmap=plt.cm.Paired,
    response_method="predict",
    ax=ax,
    xlabel="x",
    ylabel="y",
)
x_min, x_max = disp.xx0.min(), disp.xx0.max()
y_min, y_max = disp.xx1.min(), disp.xx1.max()
plt.axis("tight")

# Graficar los puntos de entrenamiento
for i, n, c in zip(range(2), class_names, plot_colors):
    idx = np.where(y == i)
    plt.scatter(
        X[idx, 0],
        X[idx, 1],
        c=c,
        cmap=plt.cm.Paired,
        s=20,
        edgecolor="k",
        label="Class %s" % n,
    )
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.legend(loc="upper right")

plt.title("Decision Boundary")
```
