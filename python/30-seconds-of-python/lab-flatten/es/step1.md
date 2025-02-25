# Aplanar una lista

Escribe una función de Python llamada `flatten(lst)` que tome una lista de listas como argumento y devuelva una lista aplanada. La función solo debe aplanar la lista una vez, lo que significa que cualquier lista anidada dentro de la lista original debe ser aplanada, pero cualquier lista anidada dentro de esas listas anidadas debe permanecer intacta.

Para resolver este problema, puedes usar una comprensión de lista para extraer cada valor de las sub-listas en orden.

```python
def flatten(lst):
  return [x for y in lst for x in y]
```

```python
flatten([[1, 2, 3, 4], [5, 6, 7, 8]]) # [1, 2, 3, 4, 5, 6, 7, 8]
```
