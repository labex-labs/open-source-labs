# Estableciendo Propiedades

La interfaz de pyplot nos permite establecer y obtener propiedades de objetos para visualizar datos. Podemos usar el método `setp` para establecer las propiedades de un objeto. Por ejemplo, para establecer el estilo de línea de una línea en guiones discontinúos, usamos el siguiente código:

```python
line, = plt.plot([1, 2, 3])
plt.setp(line, linestyle='--')
```

Si queremos saber los tipos válidos de argumentos, podemos proporcionar el nombre de la propiedad que queremos establecer sin un valor:

```python
plt.setp(line, 'linestyle')
```

Esto devolverá la siguiente salida:

```
linestyle: {'-', '--', '-.', ':', '', (offset, on-off-seq),...}
```

Si queremos ver todas las propiedades que se pueden establecer, y sus posibles valores, podemos usar el siguiente código:

```python
plt.setp(line)
```

Esto devolverá una larga lista de propiedades y sus posibles valores.
