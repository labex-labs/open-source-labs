# Dibujar flechas al final de los ejes (spines)

Para indicar la dirección de los ejes, se pueden dibujar flechas al final de los ejes (spines).

```python
ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
```
