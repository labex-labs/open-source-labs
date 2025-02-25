# Erstellen einer Farbskala

Wir werden eine Farbskala erstellen, um die Zuordnung zwischen Farben und `dydx`-Werten anzuzeigen. Wir werden die `colorbar`-Funktion aus `matplotlib.pyplot` verwenden, um eine Farbskala zu erstellen.

```python
line = plt.gca().add_collection(lc)
plt.colorbar(line)
```
