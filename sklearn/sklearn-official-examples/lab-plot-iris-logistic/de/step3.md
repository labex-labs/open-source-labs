# Zeigen Sie die Entscheidungsgrenzen im Streudiagramm an

Wir werden die Entscheidungsgrenzen im Streudiagramm mithilfe von DecisionBoundaryDisplay aus der scikit-learn-Bibliothek anzeigen.

```python
_, ax = plt.subplots(figsize=(4, 3))
DecisionBoundaryDisplay.from_estimator(
    logreg,
    X,
    cmap=plt.cm.Paired,
    ax=ax,
    response_method="predict",
    plot_method="pcolormesh",
    shading="auto",
    xlabel="Kelchblattlänge",
    ylabel="Kelchblattbreite",
    eps=0.5,
)

# Zeichnen Sie auch die Trainingspunkte
plt.scatter(X[:, 0], X[:, 1], c=Y, edgecolors="k", cmap=plt.cm.Paired)

plt.xticks(())
plt.yticks(())

plt.show()
```
