# Traçage des résultats de l'expérience 2

Nous traçons les résultats de la deuxième expérience en utilisant la bibliothèque `matplotlib`. Nous observons des résultats similaires à ceux de la première expérience : les métriques ajustées pour le hasard restent constamment proches de zéro tandis que les autres métriques tendent à augmenter avec des étiquetages plus fins. La mesure V-moyenne de l'étiquetage aléatoire augmente considérablement lorsque le nombre de groupes est plus proche du nombre total d'échantillons utilisés pour calculer la mesure.

```python
n_samples = 100
n_clusters_range = np.linspace(2, n_samples, 10).astype(int)

plt.figure(2)

plots = []
names = []

for marker, (score_name, score_func) in zip("d^vx.,", score_funcs):
    scores = uniform_labelings_scores(score_func, n_samples, n_clusters_range)
    plots.append(
        plt.errorbar(
            n_clusters_range,
            np.median(scores, axis=1),
            scores.std(axis=1),
            alpha=0.8,
            linewidth=2,
            marker=marker,
        )[0]
    )
    names.append(score_name)

plt.title(
    "Mesures de regroupement pour 2 étiquetages uniformes aléatoires\navec un nombre égal de groupes"
)
plt.xlabel(f"Nombre de groupes (Le nombre d'échantillons est fixé à {n_samples})")
plt.ylabel("Valeur du score")
plt.legend(plots, names)
plt.ylim(bottom=-0.05, top=1.05)
plt.show()
```
