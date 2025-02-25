# Personalizar el gráfico de barbas de viento

Podemos personalizar el gráfico de barbas de viento cambiando los parámetros de la función barbs. Por ejemplo, podemos cambiar la longitud y el punto de pivote de los vectores, rellenar los círculos para una barbilla vacía y cambiar los colores de las banderas y barras.

```python
plt.barbs(X, Y, U, V, length=8, pivot='middle', fill_empty=True, rounding=False,
          sizes=dict(emptybarb=0.25, spacing=0.2, height=0.3), flagcolor='r',
          barbcolor=['b', 'g'], flip_barb=True, barb_increments=dict(half=10, full=20, flag=100))
plt.show()
```
