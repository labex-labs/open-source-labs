# Darstellung der Ergebnisse des Experiments 2

Wir stellen die Ergebnisse des zweiten Experiments mit der Bibliothek `matplotlib` dar. Wir stellen ähnliche Ergebnisse wie im ersten Experiment fest: Die auf den Zufall angepassten Metriken bleiben konstant in der Nähe von Null, während andere Metriken mit feineren Belegungen tendenziell größer werden. Die durchschnittliche V-Maße der zufälligen Belegung steigt signifikant, wenn die Anzahl der Cluster der Gesamtzahl der zur Berechnung des Maße verwendeten Proben näher kommt.

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
    "Clustering measures for 2 random uniform labelings\nwith equal number of clusters"
)
plt.xlabel(f"Number of clusters (Number of samples is fixed to {n_samples})")
plt.ylabel("Score value")
plt.legend(plots, names)
plt.ylim(bottom=-0.05, top=1.05)
plt.show()
```
