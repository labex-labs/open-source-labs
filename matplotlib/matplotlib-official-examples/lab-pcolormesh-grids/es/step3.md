# Sombreado plano

La función `pcolormesh` en Matplotlib puede visualizar grillas bidimensionales. La especificación de la grilla con los menos supuestos es `shading='flat'` y si la grilla es una unidad más grande que los datos en cada dimensión, es decir, tiene forma `(M+1, N+1)`. En ese caso, `X` e `Y` especifican las esquinas de los cuadriláteros que se colorean con los valores en `Z`. Podemos visualizar la grilla usando el siguiente bloque de código:

```python
fig, ax = plt.subplots()
ax.pcolormesh(X, Y, Z, shading='flat', cmap='viridis')
ax.set_title('Flat Shading')
plt.show()
```
