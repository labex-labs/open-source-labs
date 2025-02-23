# Importar Matplotlib

Antes de poder comenzar a anotar gráficos con Matplotlib, primero debemos importar la biblioteca. En este paso, importaremos Matplotlib y crearemos un gráfico simple para usarlo en la anotación.

```python
import matplotlib.pyplot as plt

# Create a simple plot
fig, ax = plt.subplots()
ax.plot([0, 1, 2, 3, 4], [0, 1, 4, 9, 16])
plt.show()
```
