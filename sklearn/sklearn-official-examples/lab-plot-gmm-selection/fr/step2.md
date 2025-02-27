# Visualisation

Nous pouvons visualiser les différents composants à l'aide de Matplotlib.

```python
import matplotlib.pyplot as plt

plt.scatter(component_1[:, 0], component_1[:, 1], s=0.8)
plt.scatter(component_2[:, 0], component_2[:, 1], s=0.8)
plt.title("Composants de mélange gaussien")
plt.axis("égal")
plt.show()
```
