# Das Diagramm erstellen

Jetzt, wo wir die Daten haben, können wir das Diagramm erstellen. Zunächst erstellen wir ein Figure- und Achsenobjekt mit `plt.subplots()`. Anschließend plotten wir die Daten mit `ax.plot()`.

```python
fig, ax = plt.subplots()
ax.plot(t, s)
```
