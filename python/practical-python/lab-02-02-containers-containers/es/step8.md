# Conjuntos

Los conjuntos son colecciones de elementos únicos y no ordenados.

```python
tech_stocks = { 'IBM','AAPL','MSFT' }
# Sintaxis alternativa
tech_stocks = set(['IBM', 'AAPL', 'MSFT'])
```

Los conjuntos son útiles para las pruebas de pertenencia.

```python
>>> tech_stocks
set(['AAPL', 'IBM', 'MSFT'])
>>> 'IBM' in tech_stocks
True
>>> 'FB' in tech_stocks
False
>>>
```

Los conjuntos también son útiles para eliminar duplicados.

```python
names = ['IBM', 'AAPL', 'GOOG', 'IBM', 'GOOG', 'YHOO']

unique = set(names)
# unique = set(['IBM', 'AAPL','GOOG','YHOO'])
```

Operaciones adicionales de conjuntos:

```python
unique.add('CAT')        # Agregar un elemento
unique.remove('YHOO')    # Eliminar un elemento

s1 = { 'a', 'b', 'c'}
s2 = { 'c', 'd' }
s1 | s2                 # Unión de conjuntos { 'a', 'b', 'c', 'd' }
s1 & s2                 # Intersección de conjuntos { 'c' }
s1 - s2                 # Diferencia de conjuntos { 'a', 'b' }
```

En estos ejercicios, empiezas a construir uno de los principales programas utilizados para el resto de este curso. Realiza tu trabajo en el archivo `report.py`.
