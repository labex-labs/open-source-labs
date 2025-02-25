# Sombreado plano, grilla de la misma forma

Si la grilla tiene la misma forma que los datos en cada dimensión, no podemos usar `shading='flat'`. Históricamente, Matplotlib eliminaba silenciosamente la última fila y columna de `Z` en este caso, para coincidir con el comportamiento de Matlab. Si todavía se desea este comportamiento, simplemente elimine manualmente la última fila y columna. Podemos visualizar la grilla usando el siguiente bloque de código:

```python
fig, ax = plt.subplots()
ax.pcolormesh(x, y, Z[:-1, :-1], shading='flat', cmap='viridis')
ax.set_title('Flat Shading, Same Shape Grid')
plt.show()
```
