# Erstelle die Animationsframes

Wir werden jetzt die Frames für die Animation erstellen. Wir werden eine `for`-Schleife verwenden, um 60 Frames zu generieren. In jeder Iteration der Schleife werden wir die `x`- und `y`-Daten aktualisieren und dann ein neues Bildobjekt mit der `imshow`-Methode erstellen. Anschließend werden wir das Bildobjekt zur `ims`-Liste hinzufügen.

```python
ims = []
for i in range(60):
    x += np.pi / 15
    y += np.pi / 30
    im = ax.imshow(f(x, y), animated=True)
    if i == 0:
        ax.imshow(f(x, y))  # zeige zunächst ein Anfangsbild an
    ims.append([im])
```
