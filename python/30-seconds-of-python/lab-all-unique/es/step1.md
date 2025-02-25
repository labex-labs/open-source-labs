# Función para Verificar Duplicados en una Lista

Escribe una función de Python llamada `has_duplicates(lst)` que tome una lista como argumento y devuelva `True` si la lista tiene elementos duplicados, de lo contrario devuelve `False`.

Para resolver este problema, puedes seguir estos pasos:

1. Convierte la lista en un conjunto para eliminar los duplicados.
2. Compara la longitud del conjunto con la longitud de la lista original.
3. Si las longitudes son iguales, entonces la lista no tiene duplicados, de lo contrario tiene duplicados.

```python
def all_unique(lst):
  return len(lst) == len(set(lst))
```

```python
x = [1, 2, 3, 4, 5, 6]
y = [1, 2, 2, 3, 4, 5]
all_unique(x) # True
all_unique(y) # False
```
