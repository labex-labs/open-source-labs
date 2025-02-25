# Invertir un diccionario

## Problema

Escribe una función `invert_dictionary(obj)` que tome un diccionario `obj` como entrada y devuelva un nuevo diccionario con las claves y los valores invertidos. El diccionario de entrada tendrá valores hashables no únicos. Si dos o más claves tienen el mismo valor, la función debe agregar las claves a una lista en el diccionario de salida.

Para resolver este problema, puedes seguir estos pasos:

1. Crea un `collections.defaultdict` con `list` como el valor predeterminado para cada clave.
2. Utiliza `dictionary.items()` en combinación con un bucle para mapear los valores del diccionario a claves utilizando `dict.append()`.
3. Utiliza `dict()` para convertir el `collections.defaultdict` en un diccionario regular.

Firma de la función: `def invert_dictionary(obj: dict) -> dict:`

## Ejemplo

```python
ages = {
  'Peter': 10,
  'Isabel': 10,
  'Anna': 9,
}
invert_dictionary(ages) # { 10: ['Peter', 'Isabel'], 9: ['Anna'] }
```
