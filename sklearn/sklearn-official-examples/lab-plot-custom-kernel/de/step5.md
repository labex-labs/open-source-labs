# Entscheidungsgrenze darstellen

In diesem Schritt werden wir die Entscheidungsfläche und die Stützvektoren darstellen. Wir werden das DecisionBoundaryDisplay-Modul aus dem inspection-Modul von scikit-learn verwenden, um die Entscheidungsgrenze zu zeichnen. Wir werden auch die Trainingspunkte als Streudiagramm darstellen.

```python
ax = plt.gca()
DecisionBoundaryDisplay.from_estimator(
    clf,
    X,
    cmap=plt.cm.Paired,
    ax=ax,
    response_method="predict",
    plot_method="pcolormesh",
    shading="auto",
)

plt.scatter(X[:, 0], X[:, 1], c=Y, cmap=plt.cm.Paired, edgecolors="k")
plt.title("3-Class classification using Support Vector Machine with custom kernel")
plt.axis("tight")
plt.show()
```
