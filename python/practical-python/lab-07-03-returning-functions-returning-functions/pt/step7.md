# Exercício 7.7: Usando Closures para Evitar Repetição

Uma das características mais poderosas dos closures (fechamentos) é seu uso na geração de código repetitivo. Se você voltar ao Exercício 5.7, lembre-se do código para definir uma propriedade com verificação de tipo.

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    ...
    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected int')
        self._shares = value
    ...
```

Em vez de digitar repetidamente esse código, você pode criá-lo automaticamente usando um closure.

Crie um arquivo `typedproperty.py` e coloque o seguinte código nele:

```python
# typedproperty.py

def typedproperty(name, expected_type):
    private_name = '_' + name
    @property
    def prop(self):
        return getattr(self, private_name)

    @prop.setter
    def prop(self, value):
        if not isinstance(value, expected_type):
            raise TypeError(f'Expected {expected_type}')
        setattr(self, private_name, value)

    return prop
```

Agora, experimente definindo uma classe como esta:

```python
from typedproperty import typedproperty

class Stock:
    name = typedproperty('name', str)
    shares = typedproperty('shares', int)
    price = typedproperty('price', float)

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

Tente criar uma instância e verificar se a verificação de tipo funciona.

```python
>>> s = Stock('IBM', 50, 91.1)
>>> s.name
'IBM'
>>> s.shares = '100'
... should get a TypeError ...
>>>
```
