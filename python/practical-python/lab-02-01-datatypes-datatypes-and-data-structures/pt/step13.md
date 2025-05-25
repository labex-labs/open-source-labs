# Exercício 2.3: Algumas operações adicionais de dicionário

Se você transformar um dicionário em uma lista, obterá todas as suas chaves:

```python
>>> list(d)
['name', 'shares', 'price', 'date', 'account']
>>>
```

Da mesma forma, se você usar a instrução `for` para iterar em um dicionário, obterá as chaves:

```python
>>> for k in d:
        print('k =', k)

k = name
k = shares
k = price
k = date
k = account
>>>
```

Experimente esta variante que realiza uma pesquisa ao mesmo tempo:

```python
>>> for k in d:
        print(k, '=', d[k])

name = AA
shares = 75
price = 32.2
date = (6, 11, 2007)
account = 12345
>>>
```

Você também pode obter todas as chaves usando o método `keys()`:

```python
>>> keys = d.keys()
>>> keys
dict_keys(['name', 'shares', 'price', 'date', 'account'])
>>>
```

`keys()` é um pouco incomum, pois retorna um objeto especial `dict_keys`.

Este é um overlay (sobreposição) no dicionário original que sempre lhe dá as chaves atuais - mesmo que o dicionário mude. Por exemplo, tente isto:

```python
>>> del d['account']
>>> keys
dict_keys(['name', 'shares', 'price', 'date'])
>>>
```

Observe cuidadosamente que `'account'` desapareceu de `keys`, mesmo que você não tenha chamado `d.keys()` novamente.

Uma maneira mais elegante de trabalhar com chaves e valores juntos é usar o método `items()`. Isso lhe dá tuplas `(chave, valor)`:

```python
>>> items = d.items()
>>> items
dict_items([('name', 'AA'), ('shares', 75), ('price', 32.2), ('date', (6, 11, 2007))])
>>> for k, v in d.items():
        print(k, '=', v)

name = AA
shares = 75
price = 32.2
date = (6, 11, 2007)
>>>
```

Se você tiver tuplas como `items`, pode criar um dicionário usando a função `dict()`. Experimente:

```python
>>> items
dict_items([('name', 'AA'), ('shares', 75), ('price', 32.2), ('date', (6, 11, 2007))])
>>> d = dict(items)
>>> d
{'name': 'AA', 'shares': 75, 'price':32.2, 'date': (6, 11, 2007)}
>>>
```
