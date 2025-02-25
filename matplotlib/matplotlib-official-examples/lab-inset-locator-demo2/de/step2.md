# Erstellen einer Figur und von Teilplots

Als nächstes werden wir eine Figur und Teilplots erstellen, um unsere Daten anzuzeigen. Wir werden zwei nebeneinander liegende Teilplots erstellen, um zwei verschiedene Beispiele von vergrößerten Einzugsbereichen zu zeigen.

```python
fig, (ax, ax2) = plt.subplots(ncols=2, figsize=[6, 3])
```
