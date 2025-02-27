# Berechne den Nachbargraphen

In diesem Schritt werden wir den Nachbargraphen mit KNeighborsTransformer berechnen.

```python
# Der Transformator berechnet den Nachbargraphen mit der maximalen Anzahl
# von Nachbarn, die im Grid-Search erforderlich ist. Das Klassifizierungsmodell
# filtert den Nachbargraphen je nach Bedarf gemäß seinem eigenen n_neighbors-Parameter.
graph_model = KNeighborsTransformer(n_neighbors=max(n_neighbors_list), mode="distance")
```
