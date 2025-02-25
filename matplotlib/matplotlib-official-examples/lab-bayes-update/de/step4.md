# Erstellen der Animation

Jetzt, nachdem wir die `UpdateDist`-Klasse definiert haben, können wir die Animation mit der `FuncAnimation`-Klasse von Matplotlib erstellen. Wir erstellen ein Figurenobjekt und ein Achsenobjekt und übergeben das Achsenobjekt an die `UpdateDist`-Klasse, um eine neue Instanz der Klasse zu erstellen.

```python
fig, ax = plt.subplots()
ud = UpdateDist(ax, prob=0.7)
anim = FuncAnimation(fig, ud, frames=100, interval=100, blit=True)
plt.show()
```

Die `FuncAnimation`-Klasse nimmt mehrere Argumente entgegen:

- `fig`: das Figurenobjekt
- `ud`: die `UpdateDist`-Instanz
- `frames`: die Anzahl der zu animierenden Frames
- `interval`: die Zeit zwischen den Frames in Millisekunden
- `blit`: ob nur die Teile des Plots aktualisiert werden, die sich geändert haben
