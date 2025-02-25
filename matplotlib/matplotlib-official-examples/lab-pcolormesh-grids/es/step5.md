# Sombreado más cercano, grilla de la misma forma

Por lo general, eliminar una fila y una columna de datos no es lo que el usuario quiere decir cuando hace que `X`, `Y` y `Z` tengan todas la misma forma. Para este caso, Matplotlib permite `shading='nearest'` y centra los cuadriláteros coloreados en los puntos de la grilla. Si se pasa una grilla que no tiene la forma correcta con `shading='nearest'`, se produce un error. Podemos visualizar la grilla usando el siguiente bloque de código:

```python
fig, ax = plt.subplots()
ax.pcolormesh(X, Y, Z, shading='nearest', cmap='viridis')
ax.set_title('Nearest Shading, Same Shape Grid')
plt.show()
```
