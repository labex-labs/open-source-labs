# Formateo de cadenas

Una forma de formatear cadenas en Python 3.6+ es con `f-strings`.

```python
>>> nombre = 'IBM'
>>> acciones = 100
>>> precio = 91.1
>>> f'{nombre:>10s} {acciones:>10d} {precio:>10.2f}'
'       IBM        100      91.10'
>>>
```

La parte `{expresión:formato}` es reemplazada.

Se suele utilizar con `print`.

```python
print(f'{nombre:>10s} {acciones:>10d} {precio:>10.2f}')
```
