# Argumentos predeterminados

A veces desea que un argumento sea opcional. Si es así, asigne un valor predeterminado en la definición de la función.

```python
def read_prices(filename, debug=False):
 ...
```

Si se asigna un valor predeterminado, el argumento es opcional en las llamadas a la función.

```python
d = read_prices('prices.csv')
e = read_prices('prices.dat', True)
```

_Nota: Los argumentos con valores predeterminados deben aparecer al final de la lista de argumentos (todos los argumentos no opcionales van primero)._
