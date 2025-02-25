# Aplicar una función cuando sea verdadera

## Problema

Escribe una función llamada `when` que tome dos argumentos: una función condición `predicado` y una función a aplicar `cuando_es_verdadero`. La función `when` debe devolver una nueva función que tome un solo argumento `x`. La nueva función debe comprobar si el valor de `predicado(x)` es `True`. Si es así, la nueva función debe llamar a `cuando_es_verdadero(x)` y devolver el resultado. En caso contrario, la nueva función debe devolver `x`.

## Ejemplo

```python
def doble(x):
    return x * 2

def es_par(x):
    return x % 2 == 0

doblar_numeros_pares = when(es_par, doble)
doblar_numeros_pares(2) # 4
doblar_numeros_pares(1) # 1
```
