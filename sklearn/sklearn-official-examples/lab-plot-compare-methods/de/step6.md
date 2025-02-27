# T-verteilte stochastische Nachbar-Einbettung

Es wandelt Ähnlichkeiten zwischen Datenpunkten in bedingte Wahrscheinlichkeiten um und versucht, die Kullback-Leibler-Divergenz zwischen den bedingten Wahrscheinlichkeiten der Einbettung in einer niedrigen Dimension und der Daten in einer hohen Dimension zu minimieren.

```python
t_sne = manifold.TSNE(
    n_components=n_components,
    perplexity=30,
    init="random",
    n_iter=250,
    random_state=0,
)
S_t_sne = t_sne.fit_transform(S_points)
```
