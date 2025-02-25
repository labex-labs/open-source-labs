# Comprueba si cada elemento de una lista es verdadero

## Problema

Escribe una función llamada `every(lst, fn = lambda x: x)` que tome una lista `lst` y una función `fn` como argumentos. La función debe devolver `True` si `fn` devuelve `True` para cada elemento de la lista, y `False` en caso contrario. Si no se proporciona ninguna función, la función debe usar la función identidad (`lambda x: x`) por defecto.

Para resolver este problema, tendrás que usar la función `all()` en combinación con `map()` y la función `fn` proporcionada para comprobar si `fn` devuelve `True` para todos los elementos de la lista.

## Ejemplo

```python
every([4, 2, 3], lambda x: x > 1) # True
every([1, 2, 3]) # True
every([0, 1, 2]) # False
```
