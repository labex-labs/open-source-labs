# Tracer les résultats de l'algorithme d'espérance-maximisation

Nous allons tracer les résultats de l'algorithme d'espérance-maximisation.

```python
def plot_results(X, Y, means, covariances, index, title):
    splot = plt.subplot(5, 1, 1 + index)
    for i, (mean, covar, color) in enumerate(zip(means, covariances, color_iter)):
        v, w = linalg.eigh(covar)
        v = 2.0 * np.sqrt(2.0) * np.sqrt(v)
        u = w[0] / linalg.norm(w[0])
        # comme le DP n'utilisera pas tous les composants auxquels il a accès
        # à moins qu'il n'en ait besoin, nous ne devrions pas tracer les
        # composants redondants.
        if not np.any(Y == i):
            continue
        plt.scatter(X[Y == i, 0], X[Y == i, 1], 0.8, color=color)

        # Tracer une ellipse pour montrer le composant gaussien
        angle = np.arctan(u[1] / u[0])
        angle = 180.0 * angle / np.pi  # convertir en degrés
        ell = mpl.patches.Ellipse(mean, v[0], v[1], angle=180.0 + angle, color=color)
        ell.set_clip_box(splot.bbox)
        ell.set_alpha(0.5)
        splot.add_artist(ell)

    plt.xlim(-6.0, 4.0 * np.pi - 6.0)
    plt.ylim(-5.0, 5.0)
    plt.title(title)
    plt.xticks(())
    plt.yticks(())

plot_results(
    X, gmm.predict(X), gmm.means_, gmm.covariances_, 0, "Expectation-maximization"
)
```
