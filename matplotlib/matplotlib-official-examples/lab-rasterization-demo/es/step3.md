# Crear una figura con cuatro subtramas

Crearemos una figura con cuatro subtramas para ilustrar los diferentes aspectos de la rasterización.

```python
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, layout="constrained")
```
