# Visualisierung

Wir können die verschiedenen Komponenten mit Matplotlib visualisieren.

```python
import matplotlib.pyplot as plt

plt.scatter(component_1[:, 0], component_1[:, 1], s=0.8)
plt.scatter(component_2[:, 0], component_2[:, 1], s=0.8)
plt.title("Gaussian Mixture Komponenten")
plt.axis("equal")
plt.show()
```
