# Geração Eficiente de Classes

Agora que você entende como criar classes usando a função `type()`, vamos explorar uma maneira mais eficiente de gerar várias classes semelhantes. Este método economizará tempo e reduzirá a duplicação de código, tornando seu processo de programação mais suave.

## Entendendo as Classes Validadoras Atuais

Primeiro, precisamos abrir o arquivo `validate.py` no WebIDE. Este arquivo já contém várias classes validadoras, que são usadas para verificar se os valores atendem a certas condições. Essas classes incluem `Validator`, `Positive`, `PositiveInteger` e `PositiveFloat`. Adicionaremos uma classe base `Typed` e vários validadores específicos de tipo a este arquivo.

Para abrir o arquivo, execute o seguinte comando no terminal:

```bash
cd ~/project
```

## Adicionando a Classe Validadora Typed

Vamos começar adicionando a classe validadora `Typed`. Esta classe será usada para verificar se um valor é do tipo esperado.

```python
class Typed(Validator):
    expected_type = object  # Default, will be overridden in subclasses

    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'Expected {cls.expected_type}')
        super().check(value)
```

Neste código, `expected_type` é definido como `object` por padrão. As subclasses substituirão isso com o tipo específico que estão verificando. O método `check` usa a função `isinstance` para verificar se o valor é do tipo esperado. Caso contrário, ele levanta um `TypeError`.

Tradicionalmente, criaríamos validadores específicos de tipo assim:

```python
class Integer(Typed):
    expected_type = int

class Float(Typed):
    expected_type = float

class String(Typed):
    expected_type = str
```

No entanto, essa abordagem é repetitiva. Podemos fazer melhor usando o construtor `type()` para gerar essas classes dinamicamente.

## Gerando Validadores de Tipo Dinamicamente

Substituiremos as definições de classe individuais por uma abordagem mais eficiente.

```python
_typed_classes = [
    ('Integer', int),
    ('Float', float),
    ('String', str)
]

globals().update((name, type(name, (Typed,), {'expected_type': ty}))
                 for name, ty in _typed_classes)
```

Aqui está o que este código faz:

1.  Define uma lista de tuplas. Cada tupla contém um nome de classe e o tipo Python correspondente.
2.  Usa uma expressão geradora com a função `type()` para criar cada classe. A função `type()` recebe três argumentos: o nome da classe, uma tupla de classes base e um dicionário de atributos de classe.
3.  Usa `globals().update()` para adicionar as classes recém-criadas ao namespace global. Isso torna as classes acessíveis em todo o módulo.

Seu arquivo `validate.py` completo deve ter uma aparência semelhante a esta:

```python
# Basic validator classes

class Validator:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        self.check(value)
        instance.__dict__[self.name] = value

    @classmethod
    def check(cls, value):
        pass

class Positive(Validator):
    @classmethod
    def check(cls, value):
        if value <= 0:
            raise ValueError('Expected a positive value')
        super().check(value)

class PositiveInteger(Positive):
    @classmethod
    def check(cls, value):
        if not isinstance(value, int):
            raise TypeError('Expected an integer')
        super().check(value)

class PositiveFloat(Positive):
    @classmethod
    def check(cls, value):
        if not isinstance(value, float):
            raise TypeError('Expected a float')
        super().check(value)

class Typed(Validator):
    expected_type = object  # Default, will be overridden in subclasses

    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'Expected {cls.expected_type}')
        super().check(value)

# Generate type validators dynamically
_typed_classes = [
    ('Integer', int),
    ('Float', float),
    ('String', str)
]

globals().update((name, type(name, (Typed,), {'expected_type': ty}))
                 for name, ty in _typed_classes)
```

## Testando as Classes Geradas Dinamicamente

Agora, vamos testar nossas classes validadoras geradas dinamicamente. Primeiro, abra um shell interativo do Python.

```bash
cd ~/project
python3
```

Depois de entrar no shell do Python, importe e teste nossos validadores.

```python
from validate import Integer, Float, String

# Test the Integer validator
i = Integer()
i.__set_name__(None, 'test_int')
try:
    i.check("not an integer")
    print("Error: Check passed when it should have failed")
except TypeError as e:
    print(f"Integer validation: {e}")

# Test the String validator
s = String()
s.__set_name__(None, 'test_str')
try:
    s.check(123)
    print("Error: Check passed when it should have failed")
except TypeError as e:
    print(f"String validation: {e}")

# Add a new validator class to the list
import sys
print("Current validator classes:", [cls for cls in dir() if cls in ['Integer', 'Float', 'String']])
```

Você deve ver a saída mostrando os erros de validação de tipo. Isso indica que nossas classes geradas dinamicamente estão funcionando corretamente.

Quando terminar de testar, saia do shell do Python:

```python
exit()
```

## Expandindo a Geração Dinâmica de Classes

Se você quiser adicionar mais validadores de tipo, basta atualizar a lista `_typed_classes` em `validate.py`.

```python
_typed_classes = [
    ('Integer', int),
    ('Float', float),
    ('String', str),
    ('List', list),
    ('Dict', dict),
    ('Bool', bool)
]
```

Essa abordagem fornece uma maneira poderosa e eficiente de gerar várias classes semelhantes sem escrever código repetitivo. Ele permite que você dimensione facilmente seu aplicativo à medida que seus requisitos crescem.
