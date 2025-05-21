# Criando um Auxiliar de Estrutura Tipada

Nesta etapa, vamos construir um exemplo mais prático. Implementaremos uma função que cria classes com validação de tipo. A validação de tipo é crucial, pois garante que os dados atribuídos aos atributos da classe atendam a critérios específicos, como serem de um determinado tipo de dados ou estarem dentro de uma faixa específica. Isso ajuda a detectar erros precocemente e torna nosso código mais robusto.

## Entendendo a Classe Structure

Primeiro, precisamos abrir o arquivo `structure.py` no editor WebIDE. Este arquivo contém uma classe `Structure` básica. Esta classe fornece a funcionalidade fundamental para inicializar e representar objetos estruturados. Inicialização significa configurar o objeto com os dados fornecidos, e representação é sobre como o objeto é exibido quando o imprimimos.

Para abrir o arquivo, usaremos o seguinte comando no terminal:

```bash
cd ~/project
```

Após executar este comando, você estará no diretório correto onde o arquivo `structure.py` está localizado. Ao abrir o arquivo, você notará a classe `Structure` básica. Nosso objetivo é estender esta classe para suportar a validação de tipo.

## Implementando a Função typed_structure

Agora, vamos adicionar a função `typed_structure` ao arquivo `structure.py`. Esta função criará uma nova classe que herda da classe `Structure` e inclui os validadores especificados. Herança significa que a nova classe terá toda a funcionalidade da classe `Structure` e também poderá adicionar seus próprios recursos. Os validadores são usados para verificar se os valores atribuídos aos atributos da classe são válidos.

Aqui está o código para a função `typed_structure`:

```python
def typed_structure(clsname, **validators):
    """
    Create a Structure class with type validation.

    Parameters:
    - clsname: Name of the class to create
    - validators: Keyword arguments mapping attribute names to validator objects

    Returns:
    - A new class with the specified name and validators
    """
    cls = type(clsname, (Structure,), validators)
    return cls
```

O parâmetro `clsname` é o nome que queremos dar à nova classe. O parâmetro `validators` é um dicionário onde as chaves são os nomes dos atributos e os valores são os objetos validadores. A função `type()` é usada para criar uma nova classe dinamicamente. Ela recebe três argumentos: o nome da classe, uma tupla de classes base (neste caso, apenas a classe `Structure`) e um dicionário de atributos de classe (os validadores).

Após adicionar esta função, seu arquivo `structure.py` deve ter a seguinte aparência:

```python
# Structure class definition

class Structure:
    _fields = ()

    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError(f'Expected {len(self._fields)} arguments')

        # Set all of the positional arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)

        # Set the remaining keyword arguments
        for name, value in kwargs.items():
            setattr(self, name, value)

    def __repr__(self):
        attrs = ', '.join(f'{name}={getattr(self, name)!r}' for name in self._fields)
        return f'{type(self).__name__}({attrs})'

def typed_structure(clsname, **validators):
    """
    Create a Structure class with type validation.

    Parameters:
    - clsname: Name of the class to create
    - validators: Keyword arguments mapping attribute names to validator objects

    Returns:
    - A new class with the specified name and validators
    """
    cls = type(clsname, (Structure,), validators)
    return cls
```

## Testando a Função typed_structure

Vamos testar nossa função `typed_structure` usando os validadores do arquivo `validate.py`. Esses validadores são usados para verificar se os valores atribuídos aos atributos da classe são do tipo correto e atendem a outros critérios.

Primeiro, abra um shell interativo do Python. Usaremos os seguintes comandos no terminal:

```bash
cd ~/project
python3
```

O primeiro comando nos leva ao diretório correto, e o segundo comando inicia o shell interativo do Python.

Agora, importe os componentes necessários e crie uma estrutura tipada:

```python
from validate import String, PositiveInteger, PositiveFloat
from structure import typed_structure

# Create a Stock class with type validation
Stock = typed_structure('Stock', name=String(), shares=PositiveInteger(), price=PositiveFloat())

# Create a stock instance
s = Stock('GOOG', 100, 490.1)

# Test the instance
print(s.name)
print(s)

# Test validation
try:
    invalid_stock = Stock('AAPL', -10, 150.25)  # Should raise an error
except ValueError as e:
    print(f"Validation error: {e}")
```

Importamos os validadores `String`, `PositiveInteger` e `PositiveFloat` do arquivo `validate.py`. Em seguida, usamos a função `typed_structure` para criar uma classe `Stock` com validação de tipo. Criamos uma instância da classe `Stock` e a testamos imprimindo seus atributos. Finalmente, tentamos criar uma instância de ação inválida para testar a validação.

Você deve ver uma saída semelhante a:

```
GOOG
Stock('GOOG', 100, 490.1)
Validation error: Expected a positive value
```

Quando terminar de testar, saia do shell do Python:

```python
exit()
```

Este exemplo demonstra como podemos usar a função `type()` para criar classes personalizadas com regras de validação específicas. Essa abordagem é muito poderosa, pois nos permite gerar classes programaticamente, o que pode economizar muito tempo e tornar nosso código mais flexível.
