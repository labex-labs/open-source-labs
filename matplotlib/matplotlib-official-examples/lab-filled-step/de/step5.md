# Einrichten von Stilzyklen

Wir werden Stilzyklen für die Histogramme mithilfe von `cycler` einrichten. Wir werden drei Stilzyklen erstellen: einen für die Flächeneigenschaft, einen für das Label und einen für das Schraffierungsmuster.

```python
color_cycle = cycler(facecolor=plt.rcParams['axes.prop_cycle'][:4])
label_cycle = cycler(label=[f'set {n}' for n in range(4)])
hatch_cycle = cycler(hatch=['/', '*', '+', '|'])
```
