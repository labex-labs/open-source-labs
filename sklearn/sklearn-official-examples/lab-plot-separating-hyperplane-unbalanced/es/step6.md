# Graficar las funciones de decisión para ambos clasificadores

Vamos a graficar las funciones de decisión para ambos clasificadores utilizando la función `DecisionBoundaryDisplay` de la biblioteca `sklearn.inspection`. Estableceremos `plot_method` en `"contour"`, `colors` en `"k"` para el SVM simple y `"r"` para el SVM con pesos, `levels` en `[0]`, `alpha` en `0.5` y `linestyles` en `["-"]`. También estableceremos `ax` en `plt.gca()`.

```python
ax = plt.gca()
disp = DecisionBoundaryDisplay.from_estimator(
    clf,
    X,
    plot_method="contour",
    colors="k",
    levels=[0],
    alpha=0.5,
    linestyles=["-"],
    ax=ax,
)

wdisp = DecisionBoundaryDisplay.from_estimator(
    wclf,
    X,
    plot_method="contour",
    colors="r",
    levels=[0],
    alpha=0.5,
    linestyles=["-"],
    ax=ax,
)
```
