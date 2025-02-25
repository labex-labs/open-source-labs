# Die Grenzen des Graphen anpassen

Als nächstes werden wir die Grenzen des Graphen so anpassen, dass die diagonale Linie nicht mehr im 45-Grad-Winkel auf dem Bildschirm erscheint. Dies wird ein Szenario schaffen, in dem wir Text relativ zur Linie statt relativ zum Bildschirmkoordinatensystem rotieren müssen.

```python
# setze die Grenzen so, dass es auf dem Bildschirm nicht mehr wie 45 Grad aussieht
ax.set_xlim([-10, 20])
```
