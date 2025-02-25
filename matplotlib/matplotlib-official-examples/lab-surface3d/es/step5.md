# Personalizar el eje Z

```python
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
ax.zaxis.set_major_formatter('{x:.02f}')
```

Personalizamos el eje z utilizando la función `set_zlim()` para establecer los límites del eje z de -1.01 a 1.01. Luego utilizamos la función `set_major_locator()` para establecer el número de marcas en el eje z en 10 utilizando `LinearLocator(10)`. Finalmente, utilizamos la función `set_major_formatter()` para formatear las etiquetas de las marcas del eje z utilizando un `StrMethodFormatter`.
