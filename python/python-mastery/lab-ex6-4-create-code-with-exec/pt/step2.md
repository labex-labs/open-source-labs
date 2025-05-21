# Criando um Método **init**() Dinâmico

Agora, vamos aplicar o que aprendemos sobre a função `exec()` a um cenário de programação do mundo real. Em Python, a função `exec()` permite que você execute código Python armazenado em uma string. Nesta etapa, modificaremos a classe `Structure` para criar dinamicamente um método `__init__()`. O método `__init__()` é um método especial nas classes Python, que é chamado quando um objeto da classe é instanciado. Basearemos a criação deste método na variável de classe `_fields`, que contém uma lista de nomes de campos para a classe.

Primeiro, vamos dar uma olhada no arquivo `structure.py` existente. Este arquivo contém a implementação atual da classe `Structure` e uma classe `Stock` que herda dela. Para visualizar o conteúdo do arquivo, abra-o no WebIDE usando o seguinte comando:

```bash
cat /home/labex/project/structure.py
```

Na saída, você verá que a implementação atual usa uma abordagem manual para lidar com a inicialização de objetos. Isso significa que o código para inicializar os atributos do objeto é escrito explicitamente, em vez de ser gerado dinamicamente.

Agora, vamos modificar a classe `Structure`. Adicionaremos um método de classe `create_init()` que gerará dinamicamente o método `__init__()`. Para fazer essas alterações, abra o arquivo `structure.py` no editor WebIDE e siga estas etapas:

1. Remova os métodos `_init()` e `set_fields()` existentes da classe `Structure`. Esses métodos fazem parte da abordagem de inicialização manual, e não precisaremos mais deles, pois usaremos uma abordagem dinâmica.

2. Adicione o método de classe `create_init()` à classe `Structure`. Aqui está o código para o método:

```python
@classmethod
def create_init(cls):
    """Dynamically create an __init__ method based on _fields."""
    # Create argument string from field names
    argstr = ','.join(cls._fields)

    # Create the function code as a string
    code = f'def __init__(self, {argstr}):\n'
    for name in cls._fields:
        code += f'    self.{name} = {name}\n'

    # Execute the code and get the generated function
    locs = {}
    exec(code, locs)

    # Set the function as the __init__ method of the class
    setattr(cls, '__init__', locs['__init__'])
```

Neste método, primeiro criamos uma string `argstr` que contém todos os nomes de campos separados por vírgulas. Esta string será usada como a lista de argumentos para o método `__init__()`. Em seguida, criamos o código para o método `__init__()` como uma string. Iteramos pelos nomes dos campos e adicionamos linhas ao código que atribuem cada argumento ao atributo de objeto correspondente. Depois disso, usamos a função `exec()` para executar o código e armazenar a função gerada no dicionário `locs`. Finalmente, usamos a função `setattr()` para definir a função gerada como o método `__init__()` da classe.

3. Modifique a classe `Stock` para usar esta nova abordagem:

```python
class Stock(Structure):
    _fields = ('name', 'shares', 'price')

# Create the __init__ method for Stock
Stock.create_init()
```

Aqui, definimos o `_fields` para a classe `Stock` e, em seguida, chamamos o método `create_init()` para gerar o método `__init__()` para a classe `Stock`.

Seu arquivo `structure.py` completo agora deve ter uma aparência semelhante a esta:

```python
class Structure:
    # Restrict attribute assignment
    def __setattr__(self, name, value):
        if name.startswith('_') or name in self._fields:
            super().__setattr__(name, value)
        else:
            raise AttributeError(f"No attribute {name}")

    # String representation for debugging
    def __repr__(self):
        args = ', '.join(repr(getattr(self, name)) for name in self._fields)
        return f"{type(self).__name__}({args})"

    @classmethod
    def create_init(cls):
        """Dynamically create an __init__ method based on _fields."""
        # Create argument string from field names
        argstr = ','.join(cls._fields)

        # Create the function code as a string
        code = f'def __init__(self, {argstr}):\n'
        for name in cls._fields:
            code += f'    self.{name} = {name}\n'

        # Execute the code and get the generated function
        locs = {}
        exec(code, locs)

        # Set the function as the __init__ method of the class
        setattr(cls, '__init__', locs['__init__'])

class Stock(Structure):
    _fields = ('name', 'shares', 'price')

# Create the __init__ method for Stock
Stock.create_init()
```

Agora, vamos testar nossa implementação para garantir que ela funcione corretamente. Executaremos o arquivo de teste unitário para verificar se todos os testes são aprovados. Use os seguintes comandos:

```bash
cd /home/labex/project
python3 -m unittest test_structure.py
```

Se sua implementação estiver correta, você deverá ver que todos os testes são aprovados. Isso significa que o método `__init__()` gerado dinamicamente está funcionando conforme o esperado.

Você também pode testar a classe manualmente no shell Python. Veja como você pode fazer isso:

```python
>>> from structure import Stock
>>> s = Stock('GOOG', 100, 490.1)
>>> s
Stock('GOOG', 100, 490.1)
>>> s.shares = 50
>>> s.share = 50  # This should raise an AttributeError
Traceback (most recent call last):
  ...
AttributeError: No attribute share
```

No shell Python, primeiro importamos a classe `Stock` do arquivo `structure.py`. Em seguida, criamos uma instância da classe `Stock` e a imprimimos. Também podemos modificar o atributo `shares` do objeto. No entanto, quando tentamos definir um atributo que não existe na lista `_fields`, devemos obter um `AttributeError`.

Parabéns! Você usou com sucesso a função `exec()` para criar dinamicamente um método `__init__()` com base nos atributos da classe. Essa abordagem pode tornar seu código mais flexível e fácil de manter, especialmente ao lidar com classes que têm um número variável de atributos.
