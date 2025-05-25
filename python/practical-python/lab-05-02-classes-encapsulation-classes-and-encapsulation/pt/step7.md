# Propriedades

Existe uma abordagem alternativa ao padrão anterior.

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected int')
        self._shares = value
```

O acesso normal ao atributo agora aciona os métodos getter e setter sob `@property` e `@shares.setter`.

```python
>>> s = Stock('IBM', 50, 91.1)
>>> s.shares         # Triggers @property
50
>>> s.shares = 75    # Triggers @shares.setter
>>>
```

Com este padrão, _não há alterações_ necessárias no código-fonte. O novo _setter_ também é chamado quando há uma atribuição dentro da classe, inclusive dentro do método `__init__()`.

```python
class Stock:
    def __init__(self, name, shares, price):
        ...
        # This assignment calls the setter below
        self.shares = shares
        ...

    ...
    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected int')
        self._shares = value
```

Frequentemente, há uma confusão entre uma propriedade e o uso de nomes privados. Embora uma propriedade use internamente um nome privado como `_shares`, o restante da classe (não a propriedade) pode continuar a usar um nome como `shares`.

As propriedades também são úteis para atributos de dados computados.

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price
    ...
```

Isso permite que você retire os parênteses extras, escondendo o fato de que é realmente um método:

```python
>>> s = Stock('GOOG', 100, 490.1)
>>> s.shares # Instance variable
100
>>> s.cost   # Computed Value
49010.0
>>>
```
