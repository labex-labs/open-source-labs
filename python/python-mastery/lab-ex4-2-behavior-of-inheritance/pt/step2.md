# Construindo um Sistema de Validação com Herança

Nesta etapa, vamos construir um sistema de validação prático usando herança. Herança é um conceito poderoso em programação que permite criar novas classes com base em classes existentes. Dessa forma, você pode reutilizar código e criar programas mais organizados e modulares. Ao construir este sistema de validação, você verá como a herança pode ser usada para criar componentes de código reutilizáveis que podem ser combinados de diferentes maneiras.

## Criando a Classe Base Validator

Primeiro, precisamos criar uma classe base para nossos validadores. Para fazer isso, criaremos um novo arquivo no WebIDE. Veja como você pode fazer isso: clique em "File" > "New File", ou você pode usar o atalho do teclado. Assim que o novo arquivo estiver aberto, nomeie-o `validate.py`.

Agora, vamos adicionar algum código a este arquivo para criar uma classe base `Validator`. Esta classe servirá como a base para todos os nossos outros validadores.

```python
# validate.py
class Validator:
    @classmethod
    def check(cls, value):
        return value
```

Neste código, definimos uma classe `Validator` com um método `check`. O método `check` recebe um valor como argumento e simplesmente o retorna inalterado. O decorador `@classmethod` é usado para tornar este método um método de classe. Isso significa que podemos chamar este método na própria classe, sem ter que criar uma instância da classe.

## Adicionando Validadores de Tipo

Em seguida, adicionaremos alguns validadores que verificam o tipo de um valor. Esses validadores herdarão da classe `Validator` que acabamos de criar. Volte para o arquivo `validate.py` e adicione o seguinte código:

```python
class Typed(Validator):
    expected_type = object
    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'Expected {cls.expected_type}')
        return super().check(value)

class Integer(Typed):
    expected_type = int

class Float(Typed):
    expected_type = float

class String(Typed):
    expected_type = str
```

A classe `Typed` é uma subclasse de `Validator`. Ela tem um atributo `expected_type`, que é inicialmente definido como `object`. O método `check` na classe `Typed` verifica se o valor fornecido é do tipo esperado. Se não for, ele levanta um `TypeError`. Se o tipo estiver correto, ele chama o método `check` da classe pai usando `super().check(value)`.

As classes `Integer`, `Float` e `String` herdam de `Typed` e especificam o tipo exato que devem verificar. Por exemplo, a classe `Integer` verifica se um valor é um inteiro.

## Testando os Validadores de Tipo

Agora que criamos nossos validadores de tipo, vamos testá-los. Abra um novo terminal e inicie o interpretador Python executando o seguinte comando:

```bash
python3
```

Depois que o interpretador Python estiver em execução, podemos importar e testar nossos validadores. Aqui está algum código para testá-los:

```python
from validate import Integer, String

Integer.check(10)  # Should return 10

try:
    Integer.check('10')  # Should raise TypeError
except TypeError as e:
    print(f"Error: {e}")

String.check('10')  # Should return '10'
```

Quando você executar este código, você deve ver algo como isto:

```
10
Error: Expected <class 'int'>
'10'
```

Também podemos usar esses validadores em uma função. Vamos tentar isso:

```python
def add(x, y):
    Integer.check(x)
    Integer.check(y)
    return x + y

add(2, 2)  # Should return 4

try:
    add('2', '3')  # Should raise TypeError
except TypeError as e:
    print(f"Error: {e}")
```

Quando você executar este código, você deve ver:

```
4
Error: Expected <class 'int'>
```

## Adicionando Validadores de Valor

Até agora, criamos validadores que verificam o tipo de um valor. Agora, vamos adicionar alguns validadores que verificam o próprio valor, em vez do tipo. Volte para o arquivo `validate.py` e adicione o seguinte código:

```python
class Positive(Validator):
    @classmethod
    def check(cls, value):
        if value < 0:
            raise ValueError('Expected >= 0')
        return super().check(value)

class NonEmpty(Validator):
    @classmethod
    def check(cls, value):
        if len(value) == 0:
            raise ValueError('Must be non-empty')
        return super().check(value)
```

O validador `Positive` verifica se um valor é não negativo. Se o valor for menor que 0, ele levanta um `ValueError`. O validador `NonEmpty` verifica se um valor tem um comprimento diferente de zero. Se o comprimento for 0, ele levanta um `ValueError`.

## Compondo Validadores com Herança Múltipla

Agora, vamos combinar nossos validadores usando herança múltipla. Herança múltipla permite que uma classe herde de mais de uma classe pai. Volte para o arquivo `validate.py` e adicione o seguinte código:

```python
class PositiveInteger(Integer, Positive):
    pass

class PositiveFloat(Float, Positive):
    pass

class NonEmptyString(String, NonEmpty):
    pass
```

Essas novas classes combinam a verificação de tipo e a verificação de valor. Por exemplo, a classe `PositiveInteger` verifica se um valor é tanto um inteiro quanto não negativo. A ordem da herança é importante aqui. Os validadores são verificados na ordem especificada na definição da classe.

## Testando os Validadores Compostos

Vamos testar nossos validadores compostos. No interpretador Python, execute o seguinte código:

```python
from validate import PositiveInteger, PositiveFloat, NonEmptyString

PositiveInteger.check(10)  # Should return 10

try:
    PositiveInteger.check('10')  # Should raise TypeError
except TypeError as e:
    print(f"Error: {e}")

try:
    PositiveInteger.check(-10)  # Should raise ValueError
except ValueError as e:
    print(f"Error: {e}")

NonEmptyString.check('hello')  # Should return 'hello'

try:
    NonEmptyString.check('')  # Should raise ValueError
except ValueError as e:
    print(f"Error: {e}")
```

Quando você executar este código, você deve ver:

```
10
Error: Expected <class 'int'>
Error: Expected >= 0
'hello'
Error: Must be non-empty
```

Isso mostra como podemos combinar validadores para criar regras de validação mais complexas.

Quando terminar de testar, você pode sair do interpretador Python executando o seguinte comando:

```python
exit()
```
