# Ejercicio 2.18: Tabulando con Contadores

Supongamos que quisieras tabular el número total de acciones de cada empresa. Esto es fácil usando objetos `Counter`. Intenta hacerlo:

```python
>>> portfolio = read_portfolio('portfolio.csv')
>>> from collections import Counter
>>> holdings = Counter()
>>> for s in portfolio:
        holdings[s['name']] += s['shares']

>>> holdings
Counter({'MSFT': 250, 'IBM': 150, 'CAT': 150, 'AA': 100, 'GE': 95})
>>>
```

Observa cuidadosamente cómo las múltiples entradas de `MSFT` y `IBM` en `portfolio` se combinan en una sola entrada aquí.

Puedes usar un `Counter` exactamente como un diccionario para recuperar valores individuales:

```python
>>> holdings['IBM']
150
>>> holdings['MSFT']
250
>>>
```

Si quieres clasificar los valores, haz esto:

```python
>>> # Obtener las tres empresas con más acciones
>>> holdings.most_common(3)
[('MSFT', 250), ('IBM', 150), ('CAT', 150)]
>>>
```

Tomemos otra cartera de acciones y creemos un nuevo `Counter`:

```python
>>> portfolio2 = read_portfolio('portfolio2.csv')
>>> holdings2 = Counter()
>>> for s in portfolio2:
          holdings2[s['name']] += s['shares']

>>> holdings2
Counter({'HPQ': 250, 'GE': 125, 'AA': 50, 'MSFT': 25})
>>>
```

Finalmente, combinemos todas las carteras con una operación simple:

```python
>>> holdings
Counter({'MSFT': 250, 'IBM': 150, 'CAT': 150, 'AA': 100, 'GE': 95})
>>> holdings2
Counter({'HPQ': 250, 'GE': 125, 'AA': 50, 'MSFT': 25})
>>> combined = holdings + holdings2
>>> combined
Counter({'MSFT': 275, 'HPQ': 250, 'GE': 220, 'AA': 150, 'IBM': 150, 'CAT': 150})
>>>
```

Esto es solo un pequeño ejemplo de lo que ofrecen los contadores. Sin embargo, si alguna vez te encuentras necesitando tabular valores, deberías considerar usar uno.
