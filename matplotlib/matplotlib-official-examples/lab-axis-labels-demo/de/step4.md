# Die Position der Farbskalenbeschriftung festlegen

Wir können die Position der Farbskalenbeschriftung mit der `colorbar`-Methode und der `set_label`-Methode festlegen. Wir können die Position auf `'top'` (oben), `'bottom'` (unten), `'left'` (links) oder `'right'` (rechts) setzen. In diesem Beispiel setzen wir die Position auf `'top'`.

```python
cbar = fig.colorbar(sc)
cbar.set_label("ZLabel", loc='top')
```
