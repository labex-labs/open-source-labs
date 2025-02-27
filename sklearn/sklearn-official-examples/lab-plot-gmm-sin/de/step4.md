# Ergebnisse des EM-Algorithmus plotten

Wir werden die Ergebnisse des Expectation-Maximization-Algorithmus plotten.

```python
def plot_results(X, Y, Mittelwerte, Kovarianzen, index, Titel):
    splot = plt.subplot(5, 1, 1 + index)
    for i, (Mittelwert, Kovarianz, Farbe) in enumerate(zip(Mittelwerte, Kovarianzen, color_iter)):
        v, w = linalg.eigh(Kovarianz)
        v = 2.0 * np.sqrt(2.0) * np.sqrt(v)
        u = w[0] / linalg.norm(w[0])
        # da der DP nicht jede Komponente verwenden wird, die er zur Verfügung hat
        # es sei denn, er braucht sie, sollten wir die redundanten
        # Komponenten nicht plotten.
        if not np.any(Y == i):
            continue
        plt.scatter(X[Y == i, 0], X[Y == i, 1], 0.8, color=Farbe)

        # Zeichnen Sie eine Ellipse, um die Gaussian-Komponente anzuzeigen
        Winkel = np.arctan(u[1] / u[0])
        Winkel = 180.0 * Winkel / np.pi  # in Grad umwandeln
        ell = mpl.patches.Ellipse(Mittelwert, v[0], v[1], angle=180.0 + Winkel, color=Farbe)
        ell.set_clip_box(splot.bbox)
        ell.set_alpha(0.5)
        splot.add_artist(ell)

    plt.xlim(-6.0, 4.0 * np.pi - 6.0)
    plt.ylim(-5.0, 5.0)
    plt.title(Titel)
    plt.xticks(())
    plt.yticks(())

plot_results(
    X, gmm.predict(X), gmm.means_, gmm.covariances_, 0, "Expectation-maximization"
)
```
