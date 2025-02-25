# Elementos únicos en una lista

## Problema

Escribe una función de Python llamada `unique_elements` que tome una lista como entrada y devuelva una nueva lista que contenga solo los elementos únicos. Tu función debe realizar los siguientes pasos:

- Crea un `set` a partir de la lista para eliminar los valores duplicados.
- Devuelve una `lista` a partir del `set`.

Tu función debe tener la siguiente firma:

```python
def unique_elements(li: List) -> List:
```

## Ejemplo

```python
assert unique_elements([1, 2, 2, 3, 4, 3]) == [1, 2, 3, 4]
assert unique_elements(['a', 'b', 'c', 'a', 'd']) == ['a', 'b', 'c', 'd']
assert unique_elements([]) == []
```
