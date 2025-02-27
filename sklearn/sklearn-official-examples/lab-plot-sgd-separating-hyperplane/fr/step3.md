# Tracez l'hyperplan séparateur de la marge maximale

Enfin, nous pouvons tracer l'hyperplan séparateur de la marge maximale que nous avons obtenu en utilisant l'algorithme SVM avec SGD. Nous allons créer une grille de points en utilisant `np.meshgrid` puis calculer la fonction de décision pour chaque point de la grille en utilisant la méthode `decision_function` du modèle SVM. Nous tracerons ensuite la frontière de décision en utilisant `plt.contour` et les points de données en utilisant `plt.scatter`.

```python
# tracez la ligne, les points et les vecteurs les plus proches du plan
xx = np.linspace(-1, 5, 10)
yy = np.linspace(-1, 5, 10)

X1, X2 = np.meshgrid(xx, yy)
Z = np.empty(X1.shape)
for (i, j), val in np.ndenumerate(X1):
    x1 = val
    x2 = X2[i, j]
    p = clf.decision_function([[x1, x2]])
    Z[i, j] = p[0]
levels = [-1.0, 0.0, 1.0]
linestyles = ["dashed", "solid", "dashed"]
colors = "k"
plt.contour(X1, X2, Z, levels, colors=colors, linestyles=linestyles)
plt.scatter(X[:, 0], X[:, 1], c=Y, cmap=plt.cm.Paired, edgecolor="black", s=20)

plt.axis("tight")
plt.show()
```
