# Revisitando a Ordenação de Listas

Listas podem ser ordenadas _in-place_ (no local). Usando o método `sort`.

```python
s = [10,1,7,3]
s.sort() # s = [1,3,7,10]
```

Você pode ordenar em ordem reversa.

```python
s = [10,1,7,3]
s.sort(reverse=True) # s = [10,7,3,1]
```

Parece simples o suficiente. No entanto, como ordenamos uma lista de dicionários?

```python
[{'name': 'AA', 'price': 32.2, 'shares': 100},
{'name': 'IBM', 'price': 91.1, 'shares': 50},
{'name': 'CAT', 'price': 83.44, 'shares': 150},
{'name': 'MSFT', 'price': 51.23, 'shares': 200},
{'name': 'GE', 'price': 40.37, 'shares': 95},
{'name': 'MSFT', 'price': 65.1, 'shares': 50},
{'name': 'IBM', 'price': 70.44, 'shares': 100}]
```

Por quais critérios?

Você pode guiar a ordenação usando uma _função chave_ (_key function_). A _função chave_ é uma função que recebe o dicionário e retorna o valor de interesse para a ordenação.

```python
portfolio = [
    {'name': 'AA', 'price': 32.2, 'shares': 100},
    {'name': 'IBM', 'price': 91.1, 'shares': 50},
    {'name': 'CAT', 'price': 83.44, 'shares': 150},
    {'name': 'MSFT', 'price': 51.23, 'shares': 200},
    {'name': 'GE', 'price': 40.37, 'shares': 95},
    {'name': 'MSFT', 'price': 65.1, 'shares': 50},
    {'name': 'IBM', 'price': 70.44, 'shares': 100}
]

def stock_name(s):
    return s['name']

portfolio.sort(key=stock_name)
```

Aqui está o resultado.

```python
# Check how the dictionaries are sorted by the `name` key
[
  {'name': 'AA', 'price': 32.2, 'shares': 100},
  {'name': 'CAT', 'price': 83.44, 'shares': 150},
  {'name': 'GE', 'price': 40.37, 'shares': 95},
  {'name': 'IBM', 'price': 91.1, 'shares': 50},
  {'name': 'IBM', 'price': 70.44, 'shares': 100},
  {'name': 'MSFT', 'price': 51.23, 'shares': 200},
  {'name': 'MSFT', 'price': 65.1, 'shares': 50}
]
```
