# Melhorando a Implementação de _Descriptors_

Nesta etapa, vamos aprimorar nossa implementação de _descriptor_. Você pode ter notado que, em alguns casos, especificamos nomes de forma redundante. Isso pode tornar nosso código um pouco confuso e mais difícil de manter. Para resolver esse problema, usaremos o método `__set_name__`, um recurso útil introduzido no Python 3.6.

O método `__set_name__` é chamado automaticamente quando a classe é definida. Sua principal função é definir o nome do _descriptor_ para nós, para que não precisemos fazê-lo manualmente toda vez. Isso tornará nosso código mais limpo e eficiente.

Agora, vamos atualizar seu arquivo `validate.py` para incluir o método `__set_name__`. Veja como o código atualizado ficará:

```python
# validate.py

class Validator:
    def __init__(self, name=None):
        self.name = name

    def __set_name__(self, cls, name):
        # This gets called when the class is defined
        # It automatically sets the name of the descriptor
        if self.name is None:
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

No código acima, o método `__set_name__` na classe `Validator` verifica se o atributo `name` é `None`. Se for, ele define o `name` para o nome real do atributo usado na definição da classe. Dessa forma, não precisamos especificar o nome explicitamente ao criar instâncias das classes _descriptor_.

Agora que atualizamos o arquivo `validate.py`, podemos criar uma versão aprimorada de nossa classe `Stock`. Esta nova versão não exigirá que especifiquemos os nomes de forma redundante. Aqui está o código para a classe `Stock` aprimorada:

```python
# improved_stock.py

from validate import String, PositiveInteger, PositiveFloat

class Stock:
    name = String()  # No need to specify 'name' anymore
    shares = PositiveInteger()
    price = PositiveFloat()

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

Nesta classe `Stock`, simplesmente criamos instâncias das classes _descriptor_ `String`, `PositiveInteger` e `PositiveFloat` sem especificar os nomes. O método `__set_name__` na classe `Validator` cuidará de definir os nomes automaticamente.

Vamos testar nossa classe `Stock` aprimorada. Primeiro, abra seu terminal e navegue até o diretório do projeto. Em seguida, execute o arquivo `improved_stock.py` no modo interativo. Aqui estão os comandos para fazer isso:

```bash
cd ~/project
python3 -i improved_stock.py
```

Depois de entrar na sessão Python interativa, você pode tentar os seguintes comandos para testar a funcionalidade da classe `Stock`:

```python
s = Stock('GOOG', 100, 490.10)
print(s.name)    # Should return 'GOOG'
print(s.shares)  # Should return 100
print(s.price)   # Should return 490.1

# Try changing values
s.shares = 75
print(s.shares)  # Should return 75

# Try invalid values
try:
    s.shares = '75'  # Should raise TypeError
except TypeError as e:
    print(f"Error: {e}")

try:
    s.price = -10.5  # Should raise ValueError
except ValueError as e:
    print(f"Error: {e}")

exit()
```

Esses comandos criam uma instância da classe `Stock`, imprimem seus atributos, alteram o valor de um atributo e, em seguida, tentam definir valores inválidos para ver se os erros apropriados são gerados.

O método `__set_name__` define automaticamente o nome do _descriptor_ quando a classe é definida. Isso torna seu código mais limpo e menos redundante, pois você não precisa mais especificar o nome do atributo duas vezes.

Essa melhoria demonstra como o protocolo de _descriptor_ do Python continua a evoluir, tornando mais fácil escrever um código limpo e de fácil manutenção.
