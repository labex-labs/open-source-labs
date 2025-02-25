# Definiere die Parameter für das Balkendiagramm

Der nächste Schritt besteht darin, die Parameter für das Balkendiagramm zu definieren. Wir werden die x-Positionen für die Gruppen, die Breite der Balken und die Beschriftungen für die x-Achsenmarkierungen definieren.

```python
ind = np.arange(N)    # die x-Positionen für die Gruppen
width = 0.35         # die Breite der Balken
ax.set_xticks(ind + width / 2, labels=['G1', 'G2', 'G3', 'G4', 'G5'])
```
