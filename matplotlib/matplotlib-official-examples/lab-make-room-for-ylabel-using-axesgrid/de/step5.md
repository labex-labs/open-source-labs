# Platz für die Y-Beschriftung schaffen und Achsen anpassen

In diesem Schritt verwenden wir die `make_axes_area_auto_adjustable`-Methode, um in beiden Achsen Platz für die Y-Beschriftung zu schaffen. Wir verwenden auch den `use_axes`-Parameter, um die Achsen anzugeben, die angepasst werden sollen, und den `pad`-Parameter, um den Abstand zwischen den Achsen anzupassen.

```python
make_axes_area_auto_adjustable(ax1, pad=0.1, use_axes=[ax1, ax2])
make_axes_area_auto_adjustable(ax2, pad=0.1, use_axes=[ax1, ax2])
```
