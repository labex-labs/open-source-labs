# Den Graphen erstellen

Jetzt werden wir den Graphen mit der `subplots`-Funktion von Matplotlib erstellen. Wir werden zwei Teilgraphen erstellen, einen für vertikale Linien und einen für horizontale Linien. Wir werden die Größe der Figur auf (12, 6) setzen, um eine bessere Sichtbarkeit zu gewährleisten.

```python
# Create the plot
fig, (vax, hax) = plt.subplots(1, 2, figsize=(12, 6))
```
