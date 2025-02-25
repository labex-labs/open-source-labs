# Das Verwenden von integrierten Farbskalen

Matplotlib bietet eine Vielzahl von integrierten Farbskalen, die verwendet werden können, um Daten darzustellen. Diese Farbskalen können über ihre Namen zugegriffen werden, die in dem Modul `matplotlib.cm` aufgelistet sind.

```python
import matplotlib.pyplot as plt

# Erzeuge ein Diagramm mit der Farbskala 'viridis'
plt.imshow(data, cmap='viridis')
plt.colorbar()
```
