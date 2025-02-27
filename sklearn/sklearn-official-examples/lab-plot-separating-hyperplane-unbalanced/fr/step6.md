# Tracer les fonctions de décision pour les deux classifieurs

Nous allons tracer les fonctions de décision pour les deux classifieurs à l'aide de la fonction `DecisionBoundaryDisplay` de la bibliothèque `sklearn.inspection`. Nous définirons `plot_method` sur `"contour"`, `colors` sur `"k"` pour le SVM non pondéré et `"r"` pour le SVM pondéré, `levels` sur `[0]`, `alpha` sur `0.5` et `linestyles` sur `["-"]`. Nous définirons également `ax` sur `plt.gca()`.

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
