# Den Quiver-Plot erstellen

Mit dem definierten Gitter und der Richtung der Pfeile können wir den Quiver-Plot erstellen. In diesem Beispiel verwenden wir die `quiver`-Funktion von Matplotlib, um den Plot zu erstellen. Der `length`-Parameter setzt die Länge der Pfeile, und der `normalize`-Parameter normiert die Pfeile auf eine Länge von 1.

```python
ax.quiver(x, y, z, u, v, w, length=0.1, normalize=True)
```
