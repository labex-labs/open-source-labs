# Graficar algo en los subtramas

Graficaremos algo en los subtramas para que el usuario pueda ver el efecto del RectangleSelector y del EllipseSelector.

```python
N = 100000  # Si N es grande, se puede ver una mejora al usar blitting.
x = np.linspace(0, 10, N)

for ax in axs:
    ax.plot(x, np.sin(2*np.pi*x))  # grafica algo
```
