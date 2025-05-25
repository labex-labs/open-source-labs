# Exercício 2.17: Invertendo um dicionário

Um dicionário mapeia chaves para valores. Por exemplo, um dicionário de preços de ações.

```python
>>> prices = {
        'GOOG' : 490.1,
        'AA' : 23.45,
        'IBM' : 91.1,
        'MSFT' : 34.23
    }
>>>
```

Se você usar o método `items()`, você pode obter pares `(chave, valor)`:

```python
>>> prices.items()
dict_items([('GOOG', 490.1), ('AA', 23.45), ('IBM', 91.1), ('MSFT', 34.23)])
>>>
```

No entanto, e se você quisesse obter uma lista de pares `(valor, chave)` em vez disso? _Dica: use `zip()`._

```python
>>> pricelist = list(zip(prices.values(),prices.keys()))
>>> pricelist
[(490.1, 'GOOG'), (23.45, 'AA'), (91.1, 'IBM'), (34.23, 'MSFT')]
>>>
```

Por que você faria isso? Por um lado, isso permite que você execute certos tipos de processamento de dados nos dados do dicionário.

```python
>>> min(pricelist)
(23.45, 'AA')
>>> max(pricelist)
(490.1, 'GOOG')
>>> sorted(pricelist)
[(23.45, 'AA'), (34.23, 'MSFT'), (91.1, 'IBM'), (490.1, 'GOOG')]
>>>
```

Isso também ilustra uma característica importante das tuplas. Quando usadas em comparações, as tuplas são comparadas elemento por elemento, começando com o primeiro item. Semelhante a como as strings são comparadas caractere por caractere.

`zip()` é frequentemente usado em situações como esta, onde você precisa emparelhar dados de lugares diferentes. Por exemplo, emparelhar os nomes das colunas com os valores das colunas para criar um dicionário de valores nomeados.

Observe que `zip()` não se limita a pares. Por exemplo, você pode usá-lo com qualquer número de listas de entrada:

```python
>>> a = [1, 2, 3, 4]
>>> b = ['w', 'x', 'y', 'z']
>>> c = [0.2, 0.4, 0.6, 0.8]
>>> list(zip(a, b, c))
[(1, 'w', 0.2), (2, 'x', 0.4), (3, 'y', 0.6), (4, 'z', 0.8))]
>>>
```

Além disso, esteja ciente de que `zip()` para assim que a sequência de entrada mais curta é esgotada.

```python
>>> a = [1, 2, 3, 4, 5, 6]
>>> b = ['x', 'y', 'z']
>>> list(zip(a,b))
[(1, 'x'), (2, 'y'), (3, 'z')]
>>>
```
