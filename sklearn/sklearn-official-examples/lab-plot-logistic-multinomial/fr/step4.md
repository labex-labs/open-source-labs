# Tracer la frontière de décision du modèle de régression logistique multinomiale

Nous allons maintenant tracer la surface de décision du modèle de régression logistique multinomiale en utilisant la fonction `DecisionBoundaryDisplay` de scikit-learn. Nous définirons la méthode de réponse sur `"predict"`, la carte de couleurs sur `"plt.cm.Paired"` et tracerons également les points d'entraînement.

```python
_, ax = plt.subplots()
DecisionBoundaryDisplay.from_estimator(
        clf, X, response_method="predict", cmap=plt.cm.Paired, ax=ax
    )
plt.title("Surface de décision de LogisticRegression (multinomiale)")
plt.axis("tight")

colors = "bry"
for i, color in zip(clf.classes_, colors):
        idx = np.where(y == i)
        plt.scatter(
            X[idx, 0], X[idx, 1], c=color, cmap=plt.cm.Paired, edgecolor="black", s=20
        )
```
