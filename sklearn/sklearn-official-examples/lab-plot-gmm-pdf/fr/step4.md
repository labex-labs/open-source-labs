# Tracer l'estimation de densité

Nous allons maintenant tracer l'estimation de densité du mélange de gaussiennes. Nous allons créer une grille de points sur la plage de l'ensemble de données et calculer la log-vraisemblance négative prédite par le GMM pour chaque point. Nous allons ensuite afficher les scores prédits sous forme d'un graphique en ligne de niveau et tracer les données d'entraînement en nuage de points.

```python
# afficher les scores prédits par le modèle sous forme d'un graphique en ligne de niveau
x = np.linspace(-20.0, 30.0)
y = np.linspace(-20.0, 40.0)
X, Y = np.meshgrid(x, y)
XX = np.array([X.ravel(), Y.ravel()]).T
Z = -clf.score_samples(XX)
Z = Z.reshape(X.shape)

CS = plt.contour(
    X, Y, Z, norm=LogNorm(vmin=1.0, vmax=1000.0), levels=np.logspace(0, 3, 10)
)
CB = plt.colorbar(CS, shrink=0.8, extend="both")
plt.scatter(X_train[:, 0], X_train[:, 1], 0.8)

plt.title("Estimation de densité avec des modèles de mélange gaussien")
plt.axis("tight")
plt.show()
```
