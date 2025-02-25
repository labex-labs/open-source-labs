# Diferencia de listas basada en función

## Problema

Crea una función llamada `difference_by(a, b, fn)` que tome tres parámetros:

- `a`: una lista de elementos
- `b`: una lista de elementos
- `fn`: una función que se aplicará a cada elemento de ambas listas

La función debe devolver una lista de elementos que están en la lista `a` pero no en la lista `b`, después de aplicar la función `fn` proporcionada a cada elemento de ambas listas.

Para resolver este problema, puedes seguir estos pasos:

1. Crea un `set`, utilizando `map()` para aplicar `fn` a cada elemento en `b`.
2. Utiliza una comprensión de lista en combinación con `fn` en `a` para conservar solo los valores no contenidos en el `set` previamente creado, `_b`.

## Ejemplo

```python
difference_by([2.1, 1.2], [2.3, 3.4], floor) # [1.2]
difference_by([{ 'x': 2 }, { 'x': 1 }], [{ 'x': 1 }], lambda v : v['x'])
# [ { x: 2 } ]
```
