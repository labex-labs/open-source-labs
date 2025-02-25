# Eliminación de listas

Puedes eliminar elementos ya sea por valor del elemento o por índice:

```python
# Usando el valor
names.remove('Curtis')

# Usando el índice
del names[1]
```

La eliminación de un elemento no crea un hueco. Otros elementos se desplazarán hacia abajo para llenar el espacio vacado. Si hay más de una aparición del elemento, `remove()` eliminará solo la primera aparición.
