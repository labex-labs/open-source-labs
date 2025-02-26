# Expresiones generadoras y funciones de reducción

Las expresiones generadoras son especialmente útiles para alimentar datos a funciones como `sum()`, `min()`, `max()`, `any()`, etc. Prueba algunos ejemplos usando los datos del portafolio del ejemplo anterior. Observa detenidamente que estos ejemplos carecen de algunos corchetes cuadrados adicionales (\[\]) que aparecían al usar comprensiones de listas.

```python
>>> from readport import read_portfolio
>>> portfolio = read_portfolio('portfolio.csv')
>>> sum(s['shares']*s['price'] for s in portfolio)
44671.15
>>> min(s['shares'] for s in portfolio)
50
>>> any(s['name'] == 'IBM' for s in portfolio)
True
>>> all(s['name'] == 'IBM' for s in portfolio)
False
>>> sum(s['shares'] for s in portfolio if s['name'] == 'IBM')
150
>>>
```

Aquí hay un uso sutil de una expresión generadora para crear valores separados por comas:

```python
>>> s = ('GOOG',100,490.10)
>>> ','.join(s)
... observa que falla...
>>> ','.join(str(x) for x in s)    # Esto funciona
'GOOG,100,490.1'
>>>
```

La sintaxis en los ejemplos anteriores puede llevar un poco de acostumbrarse, pero el punto crucial es que ninguna de las operaciones crea nunca una lista completamente poblada de resultados. Esto te ahorra una gran cantidad de memoria. Sin embargo, debes asegurarte de no excederte con la sintaxis.
