# Agregar una barra de colores a la gráfica

Ahora, agregaremos una barra de colores a cada subgráfico utilizando la función `make_axes_locatable` de Matplotlib. Esta función toma un eje existente, lo agrega a un nuevo `AxesDivider` y devuelve el `AxesDivider`. Luego, el método `append_axes` del `AxesDivider` se puede utilizar para crear un nuevo eje en un lado dado ("arriba", "derecha", "abajo" o "izquierda") del eje original.

```python
ax1_divider = make_axes_locatable(ax1)
cax1 = ax1_divider.append_axes("right", size="7%", pad="2%")
cb1 = fig.colorbar(im1, cax=cax1)

ax2_divider = make_axes_locatable(ax2)
cax2 = ax2_divider.append_axes("top", size="7%", pad="2%")
cb2 = fig.colorbar(im2, cax=cax2, orientation="horizontal")
cax2.xaxis.set_ticks_position("top")
```
