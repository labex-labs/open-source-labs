# Dividir una lista basada en una función

## Problema

Escribe una función `bifurcate_by(lst, fn)` que tome una lista `lst` y una función de filtrado `fn` como argumentos. La función debe dividir la lista en dos grupos basados en el resultado de la función de filtrado. Si la función de filtrado devuelve un valor verdadero para un elemento, éste debe agregarse al primer grupo. De lo contrario, debe agregarse al segundo grupo.

Tu función debe devolver una lista de dos listas, donde la primera lista contiene todos los elementos para los cuales la función de filtrado devolvió un valor verdadero, y la segunda lista contiene todos los elementos para los cuales la función de filtrado devolvió un valor falso.

Utiliza una comprensión de lista para agregar elementos a los grupos, basado en el valor devuelto por `fn` para cada elemento.

## Ejemplo

```python
bifurcate_by(['beep', 'boop', 'foo', 'bar'], lambda x: x[0] == 'b')
# [ ['beep', 'boop', 'bar'], ['foo'] ]
```

En el ejemplo anterior, la función se llama con una lista de cadenas y una función de filtrado que verifica si el primer carácter de cada cadena es 'b'. La función devuelve una lista de dos listas, donde la primera lista contiene todas las cadenas que empiezan con 'b', y la segunda lista contiene todas las demás cadenas.
