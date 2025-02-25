# Stapeln von Subplots in eine Richtung

Um mehrere Subplots vertikal oder horizontal zu stapeln, können wir die Anzahl der Zeilen und Spalten als Argumente an die Funktion `subplots()` übergeben. Das zurückgegebene `axs`-Objekt ist ein eindimensionales numpy-Array, das die Liste der erstellten `Axes` enthält.

```python
fig, axs = plt.subplots(2)
axs[0].plot(x, y)
axs[1].plot(x, -y)
```
