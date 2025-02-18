# Mover los ejes (spines)

Por defecto, los ejes (spines) se dibujan en los bordes de la gráfica. En este caso, se desea mover los ejes izquierdo y inferior al centro de la gráfica.

```python
ax.spines[["left", "bottom"]].set_position(("data", 0))
```
