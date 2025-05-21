# Implementando Validadores Usando _Descriptors_

Nesta etapa, vamos criar um sistema de validação usando _descriptors_. Mas, primeiro, vamos entender o que são _descriptors_ e por que estamos usando-os. _Descriptors_ são objetos Python que implementam o protocolo de _descriptor_, que inclui os métodos `__get__`, `__set__` ou `__delete__`. Eles permitem que você personalize como um atributo é acessado, definido ou excluído em um objeto. Em nosso caso, usaremos _descriptors_ para criar um sistema de validação que garante a integridade dos dados. Isso significa que os dados armazenados em nossos objetos sempre atenderão a certos critérios, como ser de um tipo específico ou ter um valor positivo.

Agora, vamos começar a criar nosso sistema de validação. Criaremos um novo arquivo chamado `validate.py` no diretório do projeto. Este arquivo conterá as classes que implementam nossos validadores.

```python
# validate.py

class Validator:
    def __init__(self, name):
        self.name = name

    @classmethod
    def check(cls, value):
        return value

    def __set__(self, instance, value):
        instance.__dict__[self.name] = self.check(value)


class String(Validator):
    expected_type = str

    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'Expected {cls.expected_type}')
        return value


class PositiveInteger(Validator):
    expected_type = int

    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'Expected {cls.expected_type}')
        if value < 0:
            raise ValueError('Expected a positive value')
        return value


class PositiveFloat(Validator):
    expected_type = float

    @classmethod
    def check(cls, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Expected a number')
        if value < 0:
            raise ValueError('Expected a positive value')
        return float(value)
```

No arquivo `validate.py`, primeiro definimos uma classe base chamada `Validator`. Esta classe tem um método `__init__` que recebe um parâmetro `name`, que será usado para identificar o atributo que está sendo validado. O método `check` é um método de classe que simplesmente retorna o valor passado para ele. O método `__set__` é um método _descriptor_ que é chamado quando um atributo é definido em um objeto. Ele chama o método `check` para validar o valor e, em seguida, armazena o valor validado no dicionário do objeto.

Em seguida, definimos três subclasses de `Validator`: `String`, `PositiveInteger` e `PositiveFloat`. Cada uma dessas subclasses substitui o método `check` para realizar verificações de validação específicas. A classe `String` verifica se o valor é uma string, a classe `PositiveInteger` verifica se o valor é um inteiro positivo e a classe `PositiveFloat` verifica se o valor é um número positivo (seja um inteiro ou um float).

Agora que definimos nossos validadores, vamos modificar nossa classe `Stock` para usar esses validadores. Criaremos um novo arquivo chamado `stock_with_validators.py` e importaremos os validadores do arquivo `validate.py`.

```python
# stock_with_validators.py

from validate import String, PositiveInteger, PositiveFloat

class Stock:
    name = String('name')
    shares = PositiveInteger('shares')
    price = PositiveFloat('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, amount):
        self.shares -= amount

    def __repr__(self):
        return f'Stock({self.name!r}, {self.shares!r}, {self.price!r})'
```

No arquivo `stock_with_validators.py`, definimos a classe `Stock` e usamos os validadores como atributos de classe. Isso significa que sempre que um atributo é definido em um objeto `Stock`, o método `__set__` do validador correspondente será chamado para validar o valor. O método `__init__` inicializa os atributos do objeto `Stock`, e os métodos `cost`, `sell` e `__repr__` fornecem funcionalidade adicional.

Agora, vamos testar nossa classe `Stock` baseada em validadores. Abriremos um terminal, navegaremos até o diretório do projeto e executaremos o arquivo `stock_with_validators.py` no modo interativo.

```bash
cd ~/project
python3 -i stock_with_validators.py
```

Depois que o interpretador Python estiver em execução, podemos tentar alguns comandos para testar o sistema de validação.

```python
# Create a stock with valid values
s = Stock('GOOG', 100, 490.10)
print(s.name)    # Should return 'GOOG'
print(s.shares)  # Should return 100
print(s.price)   # Should return 490.1

# Try changing to valid values
s.shares = 75
print(s.shares)  # Should return 75

# Try setting invalid values
try:
    s.shares = '75'  # Should raise TypeError
except TypeError as e:
    print(f"Error setting shares to string: {e}")

try:
    s.shares = -50  # Should raise ValueError
except ValueError as e:
    print(f"Error setting negative shares: {e}")

exit()
```

No código de teste, primeiro criamos um objeto `Stock` com valores válidos e imprimimos seus atributos para verificar se eles estão definidos corretamente. Em seguida, tentamos alterar o atributo `shares` para um valor válido e imprimimos novamente para confirmar a alteração. Finalmente, tentamos definir o atributo `shares` para um valor inválido (uma string e um número negativo) e capturamos as exceções que são geradas pelos validadores.

Observe como nosso código agora está muito mais limpo. A classe `Stock` não precisa mais implementar todos aqueles métodos de propriedade - os validadores lidam com toda a verificação de tipo e restrições.

Os _descriptors_ nos permitiram criar um sistema de validação reutilizável que pode ser aplicado a qualquer atributo de classe. Este é um padrão poderoso para manter a integridade dos dados em sua aplicação.
