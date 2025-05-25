# Exercício 2.5: Lista de Dicionários (Dictionaries)

Pegue a função que você escreveu no Exercício 2.4 e modifique-a para representar cada ação na carteira com um dicionário em vez de uma tupla. Neste dicionário, use os nomes dos campos "name", "shares" e "price" para representar as diferentes colunas no arquivo de entrada.

Experimente esta nova função da mesma maneira que fez no Exercício 2.4.

```python
>>> portfolio = read_portfolio('/home/labex/project/portfolio.csv')
>>> portfolio
[{'name': 'AA', 'shares': 100, 'price': 32.2}, {'name': 'IBM', 'shares': 50, 'price': 91.1},
    {'name': 'CAT', 'shares': 150, 'price': 83.44}, {'name': 'MSFT', 'shares': 200, 'price': 51.23},
    {'name': 'GE', 'shares': 95, 'price': 40.37}, {'name': 'MSFT', 'shares': 50, 'price': 65.1},
    {'name': 'IBM', 'shares': 100, 'price': 70.44}]
>>> portfolio[0]
{'name': 'AA', 'shares': 100, 'price': 32.2}
>>> portfolio[1]
{'name': 'IBM', 'shares': 50, 'price': 91.1}
>>> portfolio[1]['shares']
50
>>> total = 0.0
>>> for s in portfolio:
        total += s['shares']*s['price']

>>> print(total)
44671.15
>>>
```

Aqui, você notará que os diferentes campos para cada entrada são acessados por nomes de chaves em vez de números de colunas numéricos. Isso é frequentemente preferível porque o código resultante é mais fácil de ler posteriormente.

Visualizar grandes dicionários e listas pode ser confuso. Para limpar a saída para depuração, considere usar a função `pprint`.

```python
>>> from pprint import pprint
>>> pprint(portfolio)
[{'name': 'AA', 'price': 32.2, 'shares': 100},
    {'name': 'IBM', 'price': 91.1, 'shares': 50},
    {'name': 'CAT', 'price': 83.44, 'shares': 150},
    {'name': 'MSFT', 'price': 51.23, 'shares': 200},
    {'name': 'GE', 'price': 40.37, 'shares': 95},
    {'name': 'MSFT', 'price': 65.1, 'shares': 50},
    {'name': 'IBM', 'price': 70.44, 'shares': 100}]
>>>
```
