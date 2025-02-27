# Considérez les résultats

Nous allons visualiser le modèle appris de KRR et de SVR lorsque la complexité/régularisation et la largeur de bande du noyau RBF sont optimisées à l'aide d'une recherche sur grille.

```python
import matplotlib.pyplot as plt

sv_ind = svr.best_estimator_.support_
plt.scatter(
    X[sv_ind],
    y[sv_ind],
    c="r",
    s=50,
    label="SVR support vectors",
    zorder=2,
    edgecolors=(0, 0, 0),
)
plt.scatter(X[:100], y[:100], c="k", label="données", zorder=1, edgecolors=(0, 0, 0))
plt.plot(
    X_plot,
    y_svr,
    c="r",
    label="SVR (ajustement: %.3fs, prédiction: %.3fs)" % (svr_fit, svr_predict),
)
plt.plot(
    X_plot, y_kr, c="g", label="KRR (ajustement: %.3fs, prédiction: %.3fs)" % (kr_fit, kr_predict)
)
plt.xlabel("données")
plt.ylabel("cible")
plt.title("SVR versus Kernel Ridge")
_ = plt.legend()
```
