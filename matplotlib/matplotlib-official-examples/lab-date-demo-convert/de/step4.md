# Erstellen des Graphen

Jetzt können wir den Graphen mit den Daten und den y-Werten erstellen. Zunächst erstellen wir ein Figure- und ein Axis-Objekt mit der subplots-Funktion. Anschließend erstellen wir den Graphen mit der plot-Funktion. Kopieren und einfügen Sie den folgenden Code:

```python
fig, ax = plt.subplots()
ax.plot(dates, y**2, 'o')
```
