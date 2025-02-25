# Erstellen eines Diagramms und von Teilplots

Als nächster Schritt erstellen wir ein Diagramm und Teilplots. Wir werden mit der Funktion `subplots` ein Diagramm mit zwei nebeneinander liegenden Teilplots erstellen.

```python
fig, (ax0, ax1) = plt.subplots(ncols=2, figsize=(7, 4))
```
