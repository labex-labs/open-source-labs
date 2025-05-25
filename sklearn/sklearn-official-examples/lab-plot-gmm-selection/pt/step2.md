# Visualização

Podemos visualizar os diferentes componentes usando Matplotlib.

```python
import matplotlib.pyplot as plt

plt.scatter(component_1[:, 0], component_1[:, 1], s=0.8)
plt.scatter(component_2[:, 0], component_2[:, 1], s=0.8)
plt.title("Componentes da Mistura Gaussiana")
plt.axis("equal")
plt.show()
```
