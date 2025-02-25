# Sombreado Gouraud

También se puede especificar el `sombreado Gouraud`, donde el color en los cuadriláteros se interpola linealmente entre los puntos de la grilla. Las formas de `X`, `Y` y `Z` deben ser las mismas. Podemos visualizar la grilla usando el siguiente bloque de código:

```python
fig, ax = plt.subplots()
ax.pcolormesh(X, Y, Z, shading='gouraud', cmap='viridis')
ax.set_title('Gouraud Shading')
plt.show()
```
