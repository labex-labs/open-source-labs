# Personalizar los ejes

Ahora personalizaremos los ejes de la representación gráfica tridimensional. Estableceremos las etiquetas para los ejes x, y y z utilizando los métodos `set_xlabel()`, `set_ylabel()` y `set_zlabel()` respectivamente. También estableceremos las marcas de graduación en el eje y utilizando el método `set_yticks()`.

```python
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_yticks(yticks)
```
