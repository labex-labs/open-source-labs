# Évaluer le modèle

Nous allons évaluer les performances de classification du modèle GPC entraîné. Nous allons générer une grille de points et calculer les probabilités prédites pour chaque point à l'aide du modèle entraîné.

```python
# Évaluer la fonction réelle et la probabilité prédite
res = 50
x1, x2 = np.meshgrid(np.linspace(-lim, lim, res), np.linspace(-lim, lim, res))
xx = np.vstack([x1.reshape(x1.size), x2.reshape(x2.size)]).T

y_true = g(xx)
y_prob = gp.predict_proba(xx)[:, 1]
y_true = y_true.reshape((res, res))
y_prob = y_prob.reshape((res, res))
```
