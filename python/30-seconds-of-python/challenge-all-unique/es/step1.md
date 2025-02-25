# Verificar duplicados en la función de lista

## Problema

Escribe una función de Python llamada `has_duplicates(lst)` que tome una lista como argumento y devuelva `True` si la lista tiene elementos duplicados, de lo contrario devuelve `False`.

Para resolver este problema, puedes seguir estos pasos:

1. Convierte la lista en un conjunto para eliminar los duplicados.
2. Compara la longitud del conjunto con la longitud de la lista original.
3. Si las longitudes son iguales, entonces la lista no tiene duplicados, de lo contrario tiene duplicados.

## Ejemplo

```python
has_duplicates([1, 2, 3, 4, 5]) # False
has_duplicates([1, 2, 3, 4, 5, 5]) # True
has_duplicates(['apple', 'banana', 'orange', 'banana']) # True
has_duplicates([]) # False
```
