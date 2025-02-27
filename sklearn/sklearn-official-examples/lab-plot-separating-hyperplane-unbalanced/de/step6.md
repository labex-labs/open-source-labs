# Die Entscheidungsfunktionen beider Klassifizierer plotten

Wir werden die Entscheidungsfunktionen beider Klassifizierer mit der `DecisionBoundaryDisplay`-Funktion aus der `sklearn.inspection`-Bibliothek plotten. Wir werden `plot_method` auf `"contour"` setzen, `colors` auf `"k"` für den einfachen SVM und `"r"` für den gewichteten SVM, `levels` auf `[0]`, `alpha` auf `0.5` und `linestyles` auf `["-"]`. Wir werden auch `ax` auf `plt.gca()` setzen.

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
