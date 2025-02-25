# Establecer el formateador y el localizador de marcas de tiempo

Establecemos el formateador de marcas de tiempo del eje x en la función de formato creada en el Paso 5 utilizando el método `set_major_formatter()`. También establecemos el localizador de marcas de tiempo del eje x en `MaxNLocator(integer=True)` para garantizar que los valores de las marcas de tiempo tomen valores enteros.

```python
ax.xaxis.set_major_formatter(format_fn)
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
```
