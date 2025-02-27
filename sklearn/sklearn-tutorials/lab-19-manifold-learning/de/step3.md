# t-verteilte stochastische Nachbar-Einbettung (t-SNE)

t-SNE ist eine beliebte Methode zur Mannigfaltigkeitslernmethode, die die Affinitäten von Datenpunkten in Wahrscheinlichkeiten umwandelt. Sie ist besonders effektiv bei der Visualisierung von hochdimensionalen Daten.

```python
from sklearn.manifold import TSNE

# Erstellen einer Instanz des t-SNE-Algorithmus
tsne = TSNE(n_components=2)

# Anpassen des Algorithmus an die Daten und Transformation der Daten in den niedrigerdimensionalen Raum
X_transformed = tsne.fit_transform(X)
```
