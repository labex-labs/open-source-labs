# _Closures_ como um Gerador de Código

Nesta etapa, aprenderemos como _closures_ podem ser usados para gerar código dinamicamente. Especificamente, construiremos um sistema de verificação de tipos para atributos de classe usando _closures_.

Primeiro, vamos entender o que são _closures_. Um _closure_ é um objeto de função que lembra valores no escopo envolvente, mesmo que eles não estejam presentes na memória. Em Python, _closures_ são criados quando uma função aninhada referencia um valor de sua função envolvente.

Agora, começaremos a implementar nosso sistema de verificação de tipos.

1. Crie um novo arquivo chamado `typedproperty.py` no diretório `/home/labex/project` com o seguinte código:

```python
# typedproperty.py

def typedproperty(name, expected_type):
    """
    Cria uma propriedade com verificação de tipo.

    Args:
        name: O nome da propriedade
        expected_type: O tipo esperado do valor da propriedade

    Returns:
        Um objeto de propriedade que realiza a verificação de tipo
    """
    private_name = '_' + name

    @property
    def value(self):
        return getattr(self, private_name)

    @value.setter
    def value(self, val):
        if not isinstance(val, expected_type):
            raise TypeError(f'Expected {expected_type}')
        setattr(self, private_name, val)

    return value
```

Neste código, a função `typedproperty` é um _closure_. Ela recebe dois argumentos: `name` e `expected_type`. O decorador `@property` é usado para criar um método getter para a propriedade, que recupera o valor do atributo privado. O decorador `@value.setter` cria um método setter que verifica se o valor que está sendo definido é do tipo esperado. Caso contrário, ele levanta um `TypeError`.

2. Agora, vamos criar uma classe que usa essas propriedades tipadas. Crie um arquivo chamado `stock.py` com o seguinte código:

```python
from typedproperty import typedproperty

class Stock:
    """Uma classe representando uma ação com atributos com verificação de tipo."""

    name = typedproperty('name', str)
    shares = typedproperty('shares', int)
    price = typedproperty('price', float)

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

Na classe `Stock`, usamos a função `typedproperty` para criar atributos com verificação de tipo para `name`, `shares` e `price`. Quando criamos uma instância da classe `Stock`, a verificação de tipo será aplicada automaticamente.

3. Vamos criar um arquivo de teste para ver isso em ação. Crie um arquivo chamado `test_stock.py` com o seguinte código:

```python
from stock import Stock

# Cria uma ação com tipos corretos
s = Stock('GOOG', 100, 490.1)
print(f"Stock name: {s.name}")
print(f"Stock shares: {s.shares}")
print(f"Stock price: {s.price}")

# Tenta definir um atributo com o tipo errado
try:
    s.shares = "hundred"  # Isso deve levantar um TypeError
    print("Type check failed")
except TypeError as e:
    print(f"Type check succeeded: {e}")
```

Neste arquivo de teste, primeiro criamos um objeto `Stock` com os tipos corretos. Em seguida, tentamos definir o atributo `shares` como uma string, o que deve levantar um `TypeError` porque o tipo esperado é um inteiro.

4. Execute o arquivo de teste:

```bash
python3 test_stock.py
```

Você deve ver uma saída semelhante a:

```
Stock name: GOOG
Stock shares: 100
Stock price: 490.1
Type check succeeded: Expected <class 'int'>
```

Esta saída mostra que a verificação de tipo está funcionando corretamente.

5. Agora, vamos aprimorar `typedproperty.py` adicionando funções de conveniência para tipos comuns. Adicione o seguinte código ao final do arquivo:

```python
def String(name):
    """Cria uma propriedade string com verificação de tipo."""
    return typedproperty(name, str)

def Integer(name):
    """Cria uma propriedade inteira com verificação de tipo."""
    return typedproperty(name, int)

def Float(name):
    """Cria uma propriedade float com verificação de tipo."""
    return typedproperty(name, float)
```

Essas funções são apenas _wrappers_ (invólucros) em torno da função `typedproperty`, tornando mais fácil criar propriedades de tipos comuns.

6. Crie um novo arquivo chamado `stock_enhanced.py` que usa essas funções de conveniência:

```python
from typedproperty import String, Integer, Float

class Stock:
    """Uma classe representando uma ação com atributos com verificação de tipo."""

    name = String('name')
    shares = Integer('shares')
    price = Float('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

Esta classe `Stock` usa as funções de conveniência para criar atributos com verificação de tipo, o que torna o código mais legível.

7. Crie um arquivo de teste `test_stock_enhanced.py` para testar a versão aprimorada:

```python
from stock_enhanced import Stock

# Cria uma ação com tipos corretos
s = Stock('GOOG', 100, 490.1)
print(f"Stock name: {s.name}")
print(f"Stock shares: {s.shares}")
print(f"Stock price: {s.price}")

# Tenta definir um atributo com o tipo errado
try:
    s.price = "490.1"  # Isso deve levantar um TypeError
    print("Type check failed")
except TypeError as e:
    print(f"Type check succeeded: {e}")
```

Este arquivo de teste é semelhante ao anterior, mas testa a classe `Stock` aprimorada.

8. Execute o teste:

```bash
python3 test_stock_enhanced.py
```

Você deve ver uma saída semelhante a:

```
Stock name: GOOG
Stock shares: 100
Stock price: 490.1
Type check succeeded: Expected <class 'float'>
```

Nesta etapa, demonstramos como _closures_ podem ser usados para gerar código. A função `typedproperty` cria objetos de propriedade que realizam a verificação de tipo, e as funções `String`, `Integer` e `Float` criam propriedades especializadas para tipos comuns.
