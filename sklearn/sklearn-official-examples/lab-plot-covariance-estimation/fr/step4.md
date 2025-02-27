# Tracer les résultats

Nous traçons la vraisemblance des données non vues pour différentes valeurs du paramètre de rétrécissement et montrons les choix par validation croisée, estimations LedoitWolf et OAS.

```python
import matplotlib.pyplot as plt

fig = plt.figure()
plt.title("Covariance régularisée : vraisemblance et coefficient de rétrécissement")
plt.xlabel("Paramètre de régularisation : coefficient de rétrécissement")
plt.ylabel("Erreur : log-vraisemblance négative sur les données de test")

plt.loglog(shrinkages, negative_logliks, label="Log-vraisemblance négative")

plt.plot(plt.xlim(), 2 * [loglik_real], "--r", label="Vraisemblance de la covariance réelle")

lik_max = np.amax(negative_logliks)
lik_min = np.amin(negative_logliks)
ymin = lik_min - 6.0 * np.log((plt.ylim()[1] - plt.ylim()[0]))
ymax = lik_max + 10.0 * np.log(lik_max - lik_min)
xmin = shrinkages[0]
xmax = shrinkages[-1]

plt.vlines(
    lw.shrinkage_,
    ymin,
    -loglik_lw,
    color="magenta",
    linewidth=3,
    label="Estimation Ledoit-Wolf",
)

plt.vlines(
    oa.shrinkage_, ymin, -loglik_oa, color="purple", linewidth=3, label="Estimation OAS"
)

plt.vlines(
    cv.best_estimator_.shrinkage,
    ymin,
    -cv.best_estimator_.score(X_test),
    color="cyan",
    linewidth=3,
    label="Meilleure estimation par validation croisée",
)

plt.ylim(ymin, ymax)
plt.xlim(xmin, xmax)
plt.legend()

plt.show()
```
