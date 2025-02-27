# Mehrdimensionale Skalierung

Mehrdimensionale Skalierung (MDS) sucht eine Darstellung der Daten in einer niedrigen Dimension, bei der die Distanzen die Distanzen im ursprünglichen hochdimensionalen Raum gut widerspiegeln.

```python
md_scaling = manifold.MDS(
    n_components=n_components,
    max_iter=50,
    n_init=4,
    random_state=0,
    normalized_stress=False,
)
S_scaling = md_scaling.fit_transform(S_points)
```
