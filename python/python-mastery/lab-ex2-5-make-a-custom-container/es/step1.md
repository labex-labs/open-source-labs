# Crecimiento de listas

Las listas de Python están altamente optimizadas para realizar operaciones de `append()`. Cada vez que una lista crece, se asigna un trozo de memoria más grande del que realmente necesita con la expectativa de que se agreguen más datos a la lista más adelante. Si se agregan nuevos elementos y hay espacio disponible, la operación `append()` almacena el elemento sin asignar más memoria.

Experimente con esta característica de las listas utilizando la función `sys.getsizeof()` en una lista y agregando algunos más elementos.

```python
>>> import sys
>>> items = []
>>> sys.getsizeof(items)
64
>>> items.append(1)
>>> sys.getsizeof(items)
96
>>> items.append(2)
>>> sys.getsizeof(items)    # Observe cómo el tamaño no aumenta
96
>>> items.append(3)
>>> sys.getsizeof(items)    # Tampoco aumenta aquí
96
>>> items.append(4)
>>> sys.getsizeof(items)    # Aún no.
96
>>> items.append(5)
>>> sys.getsizeof(items)    # Observe que el tamaño ha aumentado bruscamente
128
>>>
```

Una lista almacena sus elementos por referencia. Por lo tanto, la memoria requerida para cada elemento es una sola dirección de memoria. En una máquina de 64 bits, una dirección suele ser de 8 bytes. Sin embargo, si Python se ha compilado para 32 bits, puede ser de 4 bytes y los números del ejemplo anterior serán la mitad de los mostrados.
