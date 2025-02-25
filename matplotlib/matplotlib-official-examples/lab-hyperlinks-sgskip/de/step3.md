# Erstellen eines Bilds mit einem Hyperlink

In diesem Schritt werden wir ein Bild erstellen und einen Hyperlink hinzugefügt. Hier ist der Code, um das Bild zu erstellen:

```python
fig = plt.figure()
delta = 0.025
x = y = np.arange(-3.0, 3.0, delta)
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
Z = (Z1 - Z2) * 2

im = plt.imshow(Z, interpolation='bilinear', cmap=cm.gray,
                origin='lower', extent=[-3, 3, -3, 3])
```

Um einen Hyperlink zum Bild hinzuzufügen, müssen wir die `set_url()`-Methode des Bildobjekts verwenden. Diese Methode nimmt eine URL als Argument entgegen. Hier ist der aktualisierte Code:

```python
im.set_url('https://www.google.com/')
```

Das Bild wird einen Hyperlink zu `https://www.google.com/` haben. Schließlich können wir das Diagramm als SVG-Datei speichern, indem wir `fig.savefig()` verwenden:

```python
fig.savefig('image.svg')
```
