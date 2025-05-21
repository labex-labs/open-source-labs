# Eliminando Nomes de Propriedades com _Descriptors_

Na etapa anterior, ao criar propriedades tipadas, tivemos que declarar explicitamente os nomes das propriedades. Isso é redundante porque os nomes das propriedades já estão especificados na definição da classe. Nesta etapa, usaremos _descriptors_ para nos livrarmos dessa redundância.

Um _descriptor_ em Python é um objeto especial que controla como o acesso a atributos funciona. Quando você implementa o método `__set_name__` em um _descriptor_, ele pode obter automaticamente o nome do atributo da definição da classe.

Vamos começar criando um novo arquivo.

1. Crie um novo arquivo chamado `improved_typedproperty.py` com o seguinte código:

```python
# improved_typedproperty.py

class TypedProperty:
    """
    Um descriptor que realiza a verificação de tipo.

    Este descriptor captura automaticamente o nome do atributo da definição da classe.
    """
    def __init__(self, expected_type):
        self.expected_type = expected_type
        self.name = None

    def __set_name__(self, owner, name):
        # Este método é chamado quando o descriptor é atribuído a um atributo de classe
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(f'Expected {self.expected_type}')
        instance.__dict__[self.name] = value

# Funções de conveniência
def String():
    """Cria uma propriedade string com verificação de tipo."""
    return TypedProperty(str)

def Integer():
    """Cria uma propriedade inteira com verificação de tipo."""
    return TypedProperty(int)

def Float():
    """Cria uma propriedade float com verificação de tipo."""
    return TypedProperty(float)
```

Este código define uma classe _descriptor_ chamada `TypedProperty` que verifica o tipo de valores atribuídos aos atributos. O método `__set_name__` é chamado automaticamente quando o _descriptor_ é atribuído a um atributo de classe. Isso permite que o _descriptor_ capture o nome do atributo sem que precisemos especificá-lo manualmente.

Em seguida, criaremos uma classe que usa essas propriedades tipadas aprimoradas.

2. Crie um novo arquivo chamado `stock_improved.py` que usa as propriedades tipadas aprimoradas:

```python
from improved_typedproperty import String, Integer, Float

class Stock:
    """Uma classe representando uma ação com atributos com verificação de tipo."""

    # Não há necessidade de especificar nomes de propriedades
    name = String()
    shares = Integer()
    price = Float()

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

Observe que não precisamos especificar os nomes das propriedades ao criar as propriedades tipadas. O _descriptor_ obterá automaticamente o nome do atributo da definição da classe.

Agora, vamos testar nossa classe aprimorada.

3. Crie um arquivo de teste `test_stock_improved.py` para testar a versão aprimorada:

```python
from stock_improved import Stock

# Cria uma ação com tipos corretos
s = Stock('GOOG', 100, 490.1)
print(f"Stock name: {s.name}")
print(f"Stock shares: {s.shares}")
print(f"Stock price: {s.price}")

# Tenta definir atributos com tipos errados
try:
    s.name = 123  # Deve levantar TypeError
    print("Name type check failed")
except TypeError as e:
    print(f"Name type check succeeded: {e}")

try:
    s.shares = "hundred"  # Deve levantar TypeError
    print("Shares type check failed")
except TypeError as e:
    print(f"Shares type check succeeded: {e}")

try:
    s.price = "490.1"  # Deve levantar TypeError
    print("Price type check failed")
except TypeError as e:
    print(f"Price type check succeeded: {e}")
```

Finalmente, executaremos o teste para ver se tudo funciona como esperado.

4. Execute o teste:

```bash
python3 test_stock_improved.py
```

Você deve ver uma saída semelhante a:

```
Stock name: GOOG
Stock shares: 100
Stock price: 490.1
Name type check succeeded: Expected <class 'str'>
Shares type check succeeded: Expected <class 'int'>
Price type check succeeded: Expected <class 'float'>
```

Nesta etapa, tornamos nosso sistema de verificação de tipos melhor usando _descriptors_ e o método `__set_name__`. Isso elimina a especificação redundante do nome da propriedade, tornando o código mais curto e menos propenso a erros.

O método `__set_name__` é um recurso muito útil dos _descriptors_. Ele permite que eles coletem automaticamente informações sobre como são usados em uma definição de classe. Isso pode ser usado para criar APIs que são mais fáceis de entender e usar.
