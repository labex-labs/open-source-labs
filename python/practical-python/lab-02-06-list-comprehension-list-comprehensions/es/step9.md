# Ejercicio 2.22: Extracción de datos

Muestra cómo podrías construir una lista de tuplas `(nombre, acciones)` donde `nombre` y `acciones` se tomen de `portfolio`.

```python
>>> name_shares =[ (s['name'], s['shares']) for s in portfolio ]
>>> name_shares
[('AA', 100), ('IBM', 50), ('CAT', 150), ('MSFT', 200), ('GE', 95), ('MSFT', 50), ('IBM', 100)]
>>>
```

Si cambias los corchetes (`[`, `]`) por llaves (`{`, `}`), obtienes algo conocido como una comprensión de conjunto. Esto te da valores únicos o distintos.

Por ejemplo, esto determina el conjunto de nombres de acciones únicos que aparecen en `portfolio`:

```python
>>> names = { s['name'] for s in portfolio }
>>> names
{ 'AA', 'GE', 'IBM', 'MSFT', 'CAT' }
>>>
```

Si especificas pares `clave:valor`, puedes construir un diccionario. Por ejemplo, crea un diccionario que asocie el nombre de una acción con el número total de acciones poseídas.

```python
>>> holdings = { name: 0 for name in names }
>>> holdings
{'AA': 0, 'GE': 0, 'IBM': 0, 'MSFT': 0, 'CAT': 0}
>>>
```

Esta última característica se conoce como una **comprensión de diccionario**. Hagamos una tabla:

```python
>>> for s in portfolio:
        holdings[s['name']] += s['shares']

>>> holdings
{ 'AA': 100, 'GE': 95, 'IBM': 150, 'MSFT':250, 'CAT': 150 }
>>>
```

Prueba este ejemplo que filtra el diccionario `prices` solo a aquellos nombres que aparecen en la cartera:

```python
>>> portfolio_prices = { name: prices[name] for name in names }
>>> portfolio_prices
{'AA': 9.22, 'GE': 13.48, 'IBM': 106.28, 'MSFT': 20.89, 'CAT': 35.46}
>>>
```
