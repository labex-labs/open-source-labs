# Tracer la frontière de décision

Dans cette étape, nous allons tracer la surface de décision et les vecteurs de support. Nous utiliserons le module DecisionBoundaryDisplay du module d'inspection de scikit-learn pour tracer la frontière de décision. Nous tracerons également les points d'entraînement en nuage de points.

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
plt.title("Classification à 3 classes utilisant la Machine à Vecteurs de Support avec noyau personnalisé")
plt.axis("tight")
plt.show()
```
