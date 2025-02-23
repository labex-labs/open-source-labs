# Zufallsgenerator initialisieren und Bin-Grenzen festlegen

Initialisiere den Zufallsgenerator für die Reproduzierbarkeit und definiere die Bin-Grenzen.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

# Fixing bin edges
HIST_BINS = np.linspace(-4, 4, 100)
```
