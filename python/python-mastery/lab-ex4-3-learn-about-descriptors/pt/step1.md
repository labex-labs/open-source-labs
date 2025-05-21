# Compreendendo o Protocolo de _Descriptor_

Nesta etapa, vamos aprender como os _descriptors_ funcionam em Python, criando uma classe `Stock` simples. _Descriptors_ em Python são um recurso poderoso que permite personalizar como os atributos são acessados, definidos e excluídos. O protocolo de _descriptor_ consiste em três métodos especiais: `__get__()`, `__set__()` e `__delete__()`. Esses métodos definem como o _descriptor_ se comporta quando um atributo é acessado, recebe um valor ou é excluído, respectivamente.

Primeiro, precisamos criar um novo arquivo chamado `stock.py` no diretório do projeto. Este arquivo conterá nossa classe `Stock`. Aqui está o código que você deve colocar no arquivo `stock.py`:

```python
# stock.py

class Stock:
    __slots__ = ['_name', '_shares', '_price']

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._name = value

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected an integer')
        if value < 0:
            raise ValueError('Expected a positive value')
        self._shares = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Expected a number')
        if value < 0:
            raise ValueError('Expected a positive value')
        self._price = value

    def cost(self):
        return self.shares * self.price

    def sell(self, amount):
        self.shares -= amount

    def __repr__(self):
        return f'Stock({self.name!r}, {self.shares!r}, {self.price!r})'
```

Nesta classe `Stock`, estamos usando o decorador `@property` para definir métodos _getter_ e _setter_ para os atributos `name`, `shares` e `price`. Esses métodos _getter_ e _setter_ atuam como _descriptors_, o que significa que controlam como esses atributos são acessados e definidos. Por exemplo, os métodos _setter_ validam os valores de entrada para garantir que sejam do tipo correto e dentro de uma faixa aceitável.

Agora que temos nosso arquivo `stock.py` pronto, vamos abrir um shell Python para experimentar a classe `Stock` e ver como os _descriptors_ funcionam na prática. Para fazer isso, abra seu terminal e execute os seguintes comandos:

```bash
cd ~/project
python3 -i stock.py
```

A opção `-i` no comando `python3` diz ao Python para iniciar um shell interativo após executar o arquivo `stock.py`. Dessa forma, podemos interagir diretamente com a classe `Stock` que acabamos de definir.

No shell Python, vamos criar um objeto de ação e tentar acessar seus atributos. Veja como você pode fazer isso:

```python
s = Stock('GOOG', 100, 490.10)
s.name      # Should return 'GOOG'
s.shares    # Should return 100
```

Quando você acessa os atributos `name` e `shares` do objeto `s`, o Python está realmente usando o método `__get__` do _descriptor_ nos bastidores. Os decoradores `@property` em nossa classe são implementados usando _descriptors_, o que significa que eles lidam com o acesso e a atribuição de atributos de maneira controlada.

Vamos dar uma olhada mais de perto no dicionário da classe para ver os objetos _descriptor_. O dicionário da classe contém todos os atributos e métodos definidos na classe. Você pode visualizar as chaves do dicionário da classe usando o seguinte código:

```python
Stock.__dict__.keys()
```

Você deve ver uma saída semelhante a esta:

```
dict_keys(['__module__', '__slots__', '__init__', 'name', '_name', 'shares', '_shares', 'price', '_price', 'cost', 'sell', '__repr__', '__doc__'])
```

As chaves `name`, `shares` e `price` representam os objetos _descriptor_ criados pelos decoradores `@property`.

Agora, vamos examinar como os _descriptors_ funcionam chamando manualmente seus métodos. Usaremos o _descriptor_ `shares` como exemplo. Veja como você pode fazer isso:

```python
# Get the descriptor object for 'shares'
q = Stock.__dict__['shares']

# Use the __get__ method to retrieve the value
q.__get__(s, Stock)  # Should return 100

# Use the __set__ method to set a new value
q.__set__(s, 75)
s.shares  # Should now be 75

# Try to set an invalid value
try:
    q.__set__(s, '75')  # Should raise TypeError
except TypeError as e:
    print(f"Error: {e}")
```

Quando você acessa um atributo como `s.shares`, o Python chama o método `__get__` do _descriptor_ para recuperar o valor. Quando você atribui um valor como `s.shares = 75`, o Python chama o método `__set__` do _descriptor_. O _descriptor_ pode então validar os dados e gerar erros se o valor de entrada não for válido.

Depois de terminar de experimentar a classe `Stock` e os _descriptors_, você pode sair do shell Python executando o seguinte comando:

```python
exit()
```
