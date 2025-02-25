# Color variable

En este paso, crearemos un gráfico de flujo con color variable. El parámetro `color` toma una matriz bidimensional que representa la magnitud del campo vectorial. Aquí, estamos usando el componente `U` del campo vectorial como el color.

```python
strm = plt.streamplot(X, Y, U, V, color=U, linewidth=2, cmap='autumn')
plt.colorbar(strm.lines)
plt.title('Varying Color')
plt.show()
```
