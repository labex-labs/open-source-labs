# Criando uma Classe Base de Estrutura

Agora que temos uma boa compreensão da passagem de argumentos de funções, vamos criar uma classe base reutilizável para estruturas de dados. Esta etapa é crucial porque nos ajuda a evitar escrever o mesmo código repetidamente quando criamos classes simples que contêm dados. Ao usar uma classe base, podemos simplificar nosso código e torná-lo mais eficiente.

## O Problema com Código Repetitivo

Nos exercícios anteriores, você definiu uma classe `Stock` como mostrado abaixo:

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

Dê uma olhada no método `__init__`. Você notará que ele é bastante repetitivo. Você tem que atribuir manualmente cada atributo um por um. Isso pode se tornar muito tedioso e demorado, especialmente quando você tem muitas classes com um grande número de atributos.

## Criando uma Classe Base Flexível

Vamos criar uma classe base `Structure` que pode lidar automaticamente com a atribuição de atributos. Primeiro, abra o WebIDE e crie um novo arquivo chamado `structure.py`. Em seguida, adicione o seguinte código a este arquivo:

```python
# structure.py

class Structure:
    """
    A base class for creating simple data structures.
    Automatically populates object attributes from _fields and constructor arguments.
    """
    _fields = ()

    def __init__(self, *args):
        # Check that the number of arguments matches the number of fields
        if len(args) != len(self._fields):
            raise TypeError(f"Expected {len(self._fields)} arguments")

        # Set the attributes
        for name, value in zip(self._fields, args):
            setattr(self, name, value)
```

Esta classe base tem vários recursos importantes:

1.  Ela define uma variável de classe `_fields`. Por padrão, essa variável está vazia. Essa variável conterá os nomes dos atributos que a classe terá.
2.  Ela verifica se o número de argumentos passados para o construtor corresponde ao número de campos definidos em `_fields`. Se não corresponderem, ela levanta um `TypeError`. Isso nos ajuda a detectar erros no início.
3.  Ela define os atributos do objeto usando os nomes dos campos e os valores fornecidos como argumentos. A função `setattr` é usada para definir dinamicamente os atributos.

## Testando Nossa Classe Base de Estrutura

Agora, vamos criar algumas classes de exemplo que herdam da classe base `Structure`. Adicione o seguinte código ao seu arquivo `structure.py`:

```python
# Example classes using Structure
class Stock(Structure):
    _fields = ('name', 'shares', 'price')

class Point(Structure):
    _fields = ('x', 'y')

class Date(Structure):
    _fields = ('year', 'month', 'day')
```

Para testar se nossa implementação funciona corretamente, criaremos um arquivo de teste chamado `test_structure.py`. Adicione o seguinte código a este arquivo:

```python
# test_structure.py
from structure import Stock, Point, Date

# Test Stock class
s = Stock('GOOG', 100, 490.1)
print(f"Stock name: {s.name}, shares: {s.shares}, price: {s.price}")

# Test Point class
p = Point(3, 4)
print(f"Point coordinates: ({p.x}, {p.y})")

# Test Date class
d = Date(2023, 11, 9)
print(f"Date: {d.year}-{d.month}-{d.day}")

# Test error handling
try:
    s2 = Stock('AAPL', 50)  # Missing price argument
    print("This should not print")
except TypeError as e:
    print(f"Error correctly caught: {e}")
```

Para executar o teste, abra seu terminal e execute o seguinte comando:

```bash
python3 test_structure.py
```

Você deve ver a seguinte saída:

```
Stock name: GOOG, shares: 100, price: 490.1
Point coordinates: (3, 4)
Date: 2023-11-9
Error correctly caught: Expected 3 arguments
```

Como você pode ver, nossa classe base está funcionando como esperado. Tornou muito mais fácil definir novas estruturas de dados sem ter que escrever o mesmo código boilerplate repetidamente.
