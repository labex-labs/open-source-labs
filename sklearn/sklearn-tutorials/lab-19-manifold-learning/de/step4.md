# Ergebnisse vergleichen

Vergleichen Sie die Ergebnisse der verschiedenen Algorithmen zur Mannigfaltigkeitslernmethode. Visualisieren Sie die transformierten Daten, um zu sehen, wie die Algorithmen die zugrunde liegende Struktur der Daten bewahrt haben.

```python
import matplotlib.pyplot as plt

# Erstellen eines Streudiagramms der transformierten Daten
plt.scatter(X_transformed[:, 0], X_transformed[:, 1], c=y)
plt.title('Mannigfaltigkeitslernmethode')
plt.xlabel('Komponente 1')
plt.ylabel('Komponente 2')
plt.show()
```
