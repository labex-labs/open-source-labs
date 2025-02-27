# Zeichnet die maximale Margin trennende Hyperebene

Um die maximale Margin trennende Hyperebene zu zeichnen, verwenden wir die Funktion `DecisionBoundaryDisplay.from_estimator()` aus scikit-learn. Diese Funktion zeichnet die Entscheidungsfunktion und die Support Vektoren des SVM-Classifier. Wir werden auch die Support Vektoren als Kreise ohne Füllung und einen schwarzen Rand zeichnen.

```python
from sklearn.inspection import DecisionBoundaryDisplay

# plot the decision function and support vectors
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
