# Traçage des probabilités prédites

Maintenant, nous allons tracer les probabilités prédites pour chaque point du maillage. Nous allons créer deux sous-graphiques : l'un pour le noyau RBF isotrope et l'autre pour le noyau RBF anisotrope. Nous utiliserons la méthode `predict_proba` pour obtenir les probabilités prédites pour chaque point du maillage. Nous tracerons ensuite les probabilités prédites sous forme d'un graphique en couleur sur le maillage. Nous tracerons également les points d'entraînement pour chaque espèce de fleur Iris.

```python
titles = ["Isotropic RBF", "Anisotropic RBF"]
plt.figure(figsize=(10, 5))
for i, clf in enumerate((gpc_rbf_isotropic, gpc_rbf_anisotropic)):
    # Plot the predicted probabilities. For that, we will assign a color to
    # each point in the mesh [x_min, m_max]x[y_min, y_max].
    plt.subplot(1, 2, i + 1)

    Z = clf.predict_proba(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    Z = Z.reshape((xx.shape[0], xx.shape[1], 3))
    plt.imshow(Z, extent=(x_min, x_max, y_min, y_max), origin="lower")

    # Plot also the training points
    plt.scatter(X[:, 0], X[:, 1], c=np.array(["r", "g", "b"])[y], edgecolors=(0, 0, 0))
    plt.xlabel("Sepal length")
    plt.ylabel("Sepal width")
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.xticks(())
    plt.yticks(())
    plt.title(
        "%s, LML: %.3f" % (titles[i], clf.log_marginal_likelihood(clf.kernel_.theta))
    )

plt.tight_layout()
plt.show()
```
