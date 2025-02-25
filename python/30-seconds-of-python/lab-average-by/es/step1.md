# Promedio de una lista mapeada

Escribe una función llamada `average_by(lst, fn = lambda x: x)` que tome una lista `lst` y una función `fn` como argumentos. La función `fn` se debe usar para mapear cada elemento de la lista a un valor. Luego, la función debe calcular el promedio de los valores mapeados y devolverlo.

Si no se proporciona el argumento `fn`, la función debe usar la función identidad predeterminada, que simplemente devuelve el elemento mismo.

Tu función debe cumplir con los siguientes requisitos:

- Usar `map()` para mapear cada elemento al valor devuelto por `fn`.
- Usar `sum()` para sumar todos los valores mapeados, dividir por `len(lst)`.
- Omitir el último argumento, `fn`, para usar la función identidad predeterminada.

Firma de la función: `def average_by(lst, fn = lambda x: x) -> float:`

```python
def average_by(lst, fn = lambda x: x):
  return sum(map(fn, lst), 0.0) / len(lst)
```

```python
average_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda x: x['n'])
# 5.0
```
