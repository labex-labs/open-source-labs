# Promedio

Escribe una función llamada `average` que tome dos o más números y devuelva su promedio. Tu función debe seguir estas pautas:

- Utiliza `sum()` para sumar todos los `args` proporcionados y divídelo por `len()`.
- La función debe poder manejar cualquier cantidad de argumentos.
- La función debe devolver un `float`.

```python
def average(*args):
  return sum(args, 0.0) / len(args)
```

```python
average(*[1, 2, 3]) # 2.0
average(1, 2, 3) # 2.0
```
