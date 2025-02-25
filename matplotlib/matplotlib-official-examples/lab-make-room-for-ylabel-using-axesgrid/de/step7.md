# Die Achsen anpassen und Platz für die Y-Beschriftung schaffen

In diesem Schritt verwenden wir die `add_auto_adjustable_area`-Methode, um die Achsen anzupassen und Platz für die Y-Beschriftung zu schaffen. Wir legen auch den Titel und die X-Beschriftung für die zweite Achse fest.

```python
divider.add_auto_adjustable_area(use_axes=[ax1], pad=0.1,
                                 adjust_dirs=["left"])
divider.add_auto_adjustable_area(use_axes=[ax2], pad=0.1,
                                 adjust_dirs=["right"])
divider.add_auto_adjustable_area(use_axes=[ax1, ax2], pad=0.1,
                                 adjust_dirs=["top", "bottom"])

ax1.set_yticks([0.5], labels=["very long label"])
ax2.set_title("Title")
ax2.set_xlabel("X - Label")
```
