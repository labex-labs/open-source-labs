# Aplicar función cuando sea verdadera

Escribe una función llamada `when` que tome dos argumentos: una función condición `predicado` y una función a aplicar `cuando_verdadero`. La función `when` debe devolver una nueva función que tome un solo argumento `x`. La nueva función debe comprobar si el valor de `predicado(x)` es `True`. Si es así, la nueva función debe llamar a `cuando_verdadero(x)` y devolver el resultado. En caso contrario, la nueva función debe devolver `x`.

```python
def when(predicate, when_true):
  return lambda x: when_true(x) if predicate(x) else x
```

```python
doblar_numeros_pares = when(lambda x: x % 2 == 0, lambda x : x * 2)
doblar_numeros_pares(2) # 4
doblar_numeros_pares(1) # 1
```
