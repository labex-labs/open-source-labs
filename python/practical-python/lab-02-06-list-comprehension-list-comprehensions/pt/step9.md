# Exercício 2.22: Extração de Dados

Mostre como você pode construir uma lista de tuplas `(name, shares)` onde `name` e `shares` são tomados de `portfolio`.

```python
>>> name_shares =[ (s['name'], s['shares']) for s in portfolio ]
>>> name_shares
[('AA', 100), ('IBM', 50), ('CAT', 150), ('MSFT', 200), ('GE', 95), ('MSFT', 50), ('IBM', 100)]
>>>
```

Se você mudar os colchetes (`[`,`]`) para chaves (`{`, `}`), você obtém algo conhecido como set comprehension (compreensão de conjunto). Isso fornece valores únicos ou distintos.

Por exemplo, isso determina o conjunto de nomes de ações únicos que aparecem em `portfolio`:

```python
>>> names = { s['name'] for s in portfolio }
>>> names
{ 'AA', 'GE', 'IBM', 'MSFT', 'CAT' }
>>>
```

Se você especificar pares `key:value`, você pode construir um dicionário. Por exemplo, crie um dicionário que mapeia o nome de uma ação para o número total de ações detidas.

```python
>>> holdings = { name: 0 for name in names }
>>> holdings
{'AA': 0, 'GE': 0, 'IBM': 0, 'MSFT': 0, 'CAT': 0}
>>>
```

Este último recurso é conhecido como **dictionary comprehension** (compreensão de dicionário). Vamos tabular:

```python
>>> for s in portfolio:
        holdings[s['name']] += s['shares']

>>> holdings
{ 'AA': 100, 'GE': 95, 'IBM': 150, 'MSFT':250, 'CAT': 150 }
>>>
```

Experimente este exemplo que filtra o dicionário `prices` para apenas aqueles nomes que aparecem no portfólio:

```python
>>> portfolio_prices = { name: prices[name] for name in names }
>>> portfolio_prices
{'AA': 9.22, 'GE': 13.48, 'IBM': 106.28, 'MSFT': 20.89, 'CAT': 35.46}
>>>
```
