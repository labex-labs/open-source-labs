# Tracer les résultats

Nous allons tracer les résultats pour comparer les performances des deux régresseurs. Nous utiliserons `matplotlib` pour créer un graphique en points dispersés des données de test réelles, des prédictions effectuées par l'arbre de décision aléatoire pour la régression et des prédictions effectuées par le multi-output regressor.

```python
plt.figure()
s = 50
a = 0.4
plt.scatter(y_test[:, 0], y_test[:, 1], edgecolor="k", c="navy", s=s, marker="s", alpha=a, label="Données")
plt.scatter(y_rf[:, 0], y_rf[:, 1], edgecolor="k", c="c", s=s, marker="^", alpha=a, label="Score RF=%.2f" % regr_rf.score(X_test, y_test))
plt.scatter(y_multirf[:, 0], y_multirf[:, 1], edgecolor="k", c="cornflowerblue", s=s, alpha=a, label="Score Multi RF=%.2f" % regr_multirf.score(X_test, y_test))
plt.xlim([-6, 6])
plt.ylim([-6, 6])
plt.xlabel("cible 1")
plt.ylabel("cible 2")
plt.title("Comparaison des forêts aléatoires et de l'estimateur métamulti-output")
plt.legend()
plt.show()
```
