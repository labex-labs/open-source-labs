# Comprobar duplicados en una lista

Escribe una función de Python llamada `has_duplicates(lst)` que tome una lista como argumento y devuelva `True` si la lista contiene duplicados y `False` en caso contrario.

Para resolver este problema, puedes seguir los siguientes pasos:

1. Utiliza la función `set()` para eliminar los duplicados de la lista.
2. Compara la longitud de la lista original con la longitud del conjunto. Si son iguales, entonces no hay duplicados. Si son diferentes, entonces hay duplicados.

```python
def has_duplicates(lst):
  return len(lst)!= len(set(lst))
```

```python
x = [1, 2, 3, 4, 5, 5]
y = [1, 2, 3, 4, 5]
has_duplicates(x) # True
has_duplicates(y) # False
```
