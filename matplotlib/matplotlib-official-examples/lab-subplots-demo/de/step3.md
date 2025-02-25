# Stapeln von Subplots in zwei Richtungen

Um ein Gitter von Subplots zu erstellen, können wir die Anzahl der Zeilen und Spalten als Argumente an die Funktion `subplots()` übergeben. Das zurückgegebene `axs`-Objekt ist ein zweidimensionales NumPy-Array.

```python
fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(x, y)
axs[0, 1].plot(x, y, 'tab:orange')
axs[1, 0].plot(x, -y, 'tab:green')
axs[1, 1].plot(x, -y, 'tab:red')
```
