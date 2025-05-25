# Dicionários e Objetos

Objetos definidos pelo usuário também usam dicionários tanto para dados de instância quanto para classes. De fato, todo o sistema de objetos é, em sua maior parte, uma camada extra que é colocada em cima de dicionários.

Um dicionário armazena os dados da instância, `__dict__`.

```python
>>> from stock import Stock
>>> s = Stock('GOOG', 100, 490.1)
>>> s.__dict__
{'name' : 'GOOG', 'shares' : 100, 'price': 490.1 }
```

Você preenche este dict (e instância) ao atribuir a `self`.

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

Os dados da instância, `self.__dict__`, se parecem com isto:

```python
{
    'name': 'GOOG',
    'shares': 100,
    'price': 490.1
}
```

**Cada instância recebe seu próprio dicionário privado.**

```python
s = Stock('GOOG', 100, 490.1)     # {'name' : 'GOOG','shares' : 100, 'price': 490.1 }
t = Stock('AAPL', 50, 123.45)     # {'name' : 'AAPL','shares' : 50, 'price': 123.45 }
```

Se você criasse 100 instâncias de alguma classe, haveria 100 dicionários armazenando dados.
