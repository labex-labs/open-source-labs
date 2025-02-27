# Vorcomputieren der Gram-Matrix mit gewichteten Stichproben

Um das elastische Netz mit der Option `precompute` zusammen mit den Stichprobengewichten anzupassen, müssen wir die Designmatrix zunächst zentrieren und sie vor der Berechnung der Gram-Matrix durch die normalisierten Gewichte skalieren. Wir zentrieren die Designmatrix, indem wir von jeder Zeile den gewichteten Mittelwert jeder Merkmalsspalte subtrahieren. Anschließend skalieren wir die zentrierte Designmatrix, indem wir jede Zeile mit der Quadratwurzel des entsprechenden normalisierten Gewichts multiplizieren. Schließlich berechnen wir die Gram-Matrix, indem wir das Skalarprodukt der skalierten Designmatrix mit ihrer Transponierten bilden.

```python
X_offset = np.average(X, axis=0, weights=normalized_weights)
X_centered = X - np.average(X, axis=0, weights=normalized_weights)
X_scaled = X_centered * np.sqrt(normalized_weights)[:, np.newaxis]
gram = np.dot(X_scaled.T, X_scaled)
```
