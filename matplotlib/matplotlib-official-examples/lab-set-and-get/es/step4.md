# Obteniendo Propiedades

Podemos usar el método `getp` para obtener las propiedades de un objeto. Lo podemos usar para consultar el valor de un atributo único:

```python
plt.getp(line, 'linewidth')
```

Esto devolverá el valor de la propiedad de ancho de línea del objeto de línea.

También podemos usar `getp` para obtener todos los pares atributo/valor de un objeto:

```python
plt.getp(line)
```

Esto devolverá una larga lista de todas las propiedades y sus valores.
