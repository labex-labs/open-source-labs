# Ejecutar función para cada elemento de la lista en orden inverso

## Problema

Escribe una función `for_each_right(itr, fn)` que tome una lista `itr` y una función `fn` como argumentos. La función debe ejecutar `fn` una vez para cada elemento en `itr`, comenzando desde el último.

## Ejemplo

```python
for_each_right([1, 2, 3], print) # 3 2 1
```

## Restricciones

- La función debe funcionar para cualquier lista y función.
- La función no debe modificar la lista original.
