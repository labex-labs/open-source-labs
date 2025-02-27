# Tracer l'hyperplan séparateur à marge maximale

Pour tracer l'hyperplan séparateur à marge maximale, nous utiliserons la fonction `DecisionBoundaryDisplay.from_estimator()` de scikit-learn. Cette fonction trace la fonction de décision et les vecteurs de support du classifieur SVM. Nous tracerons également les vecteurs de support sous forme de cercles sans remplissage et avec une bordure noire.

```python
from sklearn.inspection import DecisionBoundaryDisplay

# tracer la fonction de décision et les vecteurs de support
ax = plt.gca()
DecisionBoundaryDisplay.from_estimator(
    clf,
    X,
    plot_method="contour",
    colors="k",
    levels=[-1, 0, 1],
    alpha=0.5,
    linestyles=["--", "-", "--"],
    ax=ax,
)
ax.scatter(
    clf.support_vectors_[:, 0],
    clf.support_vectors_[:, 1],
    s=100,
    linewidth=1,
    facecolors="none",
    edgecolors="k",
)
plt.show()
```
