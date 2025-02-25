# Ajustar los límites y agregar etiquetas

Finalmente, ajustaremos los límites de la gráfica y agregaremos etiquetas de eje utilizando las funciones `set_zlim()`, `set_xlabel()`, `set_ylabel()` y `set_zlabel()` de Matplotlib. También usaremos el modo de matemáticas LaTeX para escribir las etiquetas de eje.

```python
ax.set_zlim(0, 1)
ax.set_xlabel(r'$\phi_\mathrm{real}$')
ax.set_ylabel(r'$\phi_\mathrm{im}$')
ax.set_zlabel(r'$V(\phi)$')
```
