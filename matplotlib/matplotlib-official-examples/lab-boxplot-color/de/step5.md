# Füllen der Boxplots mit benutzerdefinierten Farben

Als nächstes werden wir die Boxplots mit benutzerdefinierten Farben füllen. Wir werden eine Liste von Farben erstellen und eine Schleife verwenden, um jede Box mit einer anderen Farbe zu füllen.

```python
colors = ['pink', 'lightblue', 'lightgreen']
for bplot in (bplot1, bplot2):
    for patch, color in zip(bplot['boxes'], colors):
        patch.set_facecolor(color)
```
