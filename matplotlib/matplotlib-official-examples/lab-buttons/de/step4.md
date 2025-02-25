# Erstelle die Schaltflächen **Next** und **Previous**

Jetzt werden wir die Schaltflächen **Next** und **Previous** mithilfe der `add_axes`-Funktion von `matplotlib.pyplot` erstellen und den zuvor erstellten Callback-Funktionen zuweisen, indem wir `on_clicked` verwenden.

```python
axprev = fig.add_axes([0.7, 0.05, 0.1, 0.075])
axnext = fig.add_axes([0.81, 0.05, 0.1, 0.075])
bnext = Button(axnext, 'Next')
bnext.on_clicked(callback.next)
bprev = Button(axprev, 'Previous')
bprev.on_clicked(callback.prev)
```
