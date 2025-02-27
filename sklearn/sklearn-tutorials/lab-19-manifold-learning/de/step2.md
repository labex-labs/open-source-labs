# Lokale lineare Einbettung (Locally Linear Embedding, LLE)

Die Lokale lineare Einbettung (LLE) ist ein weiterer Algorithmus zur Mannigfaltigkeitslernmethode. Sie sucht eine niedrigerdimensionale Projektion der Daten, die die Distanzen innerhalb lokaler Nachbarschaften erhält.

```python
from sklearn.manifold import LocallyLinearEmbedding

# Erstellen einer Instanz des LLE-Algorithmus
lle = LocallyLinearEmbedding(n_components=2)

# Anpassen des Algorithmus an die Daten und Transformation der Daten in den niedrigerdimensionalen Raum
X_transformed = lle.fit_transform(X)
```
