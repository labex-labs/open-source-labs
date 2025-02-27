# Multi-dimensionale Skalierung (MDS) durchführen

Anschließend werden wir MDS auf dem rauschenden Datensatz mit der MDS-Klasse von scikit-learn durchführen. Wir werden die Option für die vorgeberechnete Ungleichartigkeit verwenden, da wir bereits die paarweisen Distanzen zwischen den Datenpunkten berechnet haben. Wir werden auch die Anzahl der Komponenten auf 2 für die 2D-Visualisierung setzen.

```python
mds = manifold.MDS(
    n_components=2,
    max_iter=3000,
    eps=1e-9,
    random_state=seed,
    dissimilarity="precomputed",
    n_jobs=1,
    normalized_stress="auto",
)
pos = mds.fit(similarities).embedding_
```
