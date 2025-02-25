# Funktion zur Einrichtung von Achsen definieren

Um den Code zu vereinfachen, können wir eine Funktion definieren, die ein Figurobjekt und eine Position als Eingabe nimmt und ein Achsenobjekt mit benutzerdefinierten Skalenbeschriftungen zurückgibt.

```python
def setup_axes(fig, pos):
    ax = fig.add_subplot(pos, axes_class=axisartist.Axes)
    ax.set_yticks([0.2, 0.8], labels=["short", "loooong"])
    ax.set_xticks([0.2, 0.8], labels=[r"$\frac{1}{2}\pi$", r"$\pi$"])
    return ax
```
