# Subplots erstellen

Wir erstellen drei Subplots mit der `subplots`-Funktion in Matplotlib. Wir setzen den Parameter `sharex` auf `True`, um sicherzustellen, dass die Subplots eine gemeinsame x-Achse teilen. Wir entfernen auch den vertikalen Abstand zwischen den Subplots mit der `subplots_adjust`-Funktion.

```python
fig, axs = plt.subplots(3, 1, sharex=True)
fig.subplots_adjust(hspace=0)
```
