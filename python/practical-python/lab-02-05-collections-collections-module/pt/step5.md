# Exercício 2.18: Tabulação com Contadores

Suponha que você queira tabular o número total de ações de cada ação. Isso é fácil usando objetos `Counter`. Tente:

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

Observe cuidadosamente como as múltiplas entradas para `MSFT` e `IBM` em `portfolio` são combinadas em uma única entrada aqui.

Você pode usar um Counter como um dicionário para recuperar valores individuais:

```python
>>> holdings['IBM']
150
>>> holdings['MSFT']
250
>>>
```

Se você quiser classificar os valores, faça o seguinte:

```python
>>> # Obter as três ações mais detidas
>>> holdings.most_common(3)
[('MSFT', 250), ('IBM', 150), ('CAT', 150)]
>>>
```

Vamos pegar outro portfólio de ações e criar um novo Counter:

```python
>>> portfolio2 = read_portfolio('portfolio2.csv')
>>> holdings2 = Counter()
>>> for s in portfolio2:
          holdings2[s['name']] += s['shares']

>>> holdings2
Counter({'HPQ': 250, 'GE': 125, 'AA': 50, 'MSFT': 25})
>>>
```

Finalmente, vamos combinar todas as participações fazendo uma operação simples:

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

Este é apenas um pequeno exemplo do que os contadores fornecem. No entanto, se você precisar tabular valores, deve considerar o uso de um.
