# Anzeigeobjekte in einem einzigen Plot kombinieren

Die Anzeigeobjekte speichern die berechneten Werte, die als Argumente übergeben wurden. Dies ermöglicht es, die Visualisierungen mit der API von Matplotlib leicht zu kombinieren. Im folgenden Beispiel platzieren wir die Anzeigen nebeneinander in einer Zeile.

```python
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 8))

roc_display.plot(ax=ax1)
pr_display.plot(ax=ax2)
plt.show()
```
