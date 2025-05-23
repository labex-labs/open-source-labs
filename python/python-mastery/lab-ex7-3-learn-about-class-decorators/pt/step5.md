# Adicionando Validação de Argumentos de Método

Em Python, validar dados é uma parte importante da escrita de código robusto. Nesta seção, levaremos nossa validação um passo adiante, validando automaticamente os argumentos do método. O arquivo `validate.py` já inclui um decorador `@validated`. Um decorador em Python é uma função especial que pode modificar outra função. O decorador `@validated` aqui pode verificar os argumentos da função em relação às suas anotações. Anotações em Python são uma maneira de adicionar metadados aos parâmetros da função e aos valores de retorno.

Vamos modificar nosso código para aplicar este decorador a métodos com anotações:

1. Primeiro, precisamos entender como o decorador `validated` funciona. Abra o arquivo `validate.py` para revisá-lo:

```bash
code ~/project/validate.py
```

O decorador `validated` usa anotações de função para validar argumentos. Antes de permitir que a função seja executada, ele verifica cada argumento em relação ao seu tipo de anotação. Por exemplo, se um argumento for anotado como um inteiro, o decorador garantirá que o valor passado seja de fato um inteiro.

2. Agora, modificaremos a função `validate_attributes` em `structure.py` para envolver métodos anotados com o decorador `validated`. Isso significa que qualquer método com anotações na classe terá seus argumentos validados automaticamente. Abra o arquivo `structure.py`:

```bash
code ~/project/structure.py
```

3. Atualize a função `validate_attributes`:

```python
def validate_attributes(cls):
    """
    Class decorator that:
    1. Extracts Validator instances and builds _fields and _types lists
    2. Applies @validated decorator to methods with annotations
    """
    # Import the validated decorator
    from validate import validated

    # Process validator descriptors
    validators = []
    for name, val in vars(cls).items():
        if isinstance(val, Validator):
            validators.append(val)

    # Set _fields based on validator names
    cls._fields = [val.name for val in validators]

    # Set _types based on validator expected_types
    cls._types = [getattr(val, 'expected_type', lambda x: x) for val in validators]

    # Apply @validated decorator to methods with annotations
    for name, val in vars(cls).items():
        if callable(val) and hasattr(val, '__annotations__'):
            setattr(cls, name, validated(val))

    # Create initialization method
    cls.create_init()

    return cls
```

Esta função atualizada agora faz o seguinte:

1. Processa os descritores de validador como antes. Descritores de validador são usados para definir regras de validação para atributos de classe.
2. Encontra todos os métodos com anotações na classe. Anotações são adicionadas aos parâmetros do método para especificar o tipo esperado do argumento.
3. Aplica o decorador `@validated` a esses métodos. Isso garante que os argumentos passados para esses métodos sejam validados de acordo com suas anotações.

4. Salve o arquivo após fazer essas alterações. Salvar o arquivo é importante porque garante que nossas modificações sejam armazenadas e possam ser usadas posteriormente.

5. Agora, vamos atualizar o método `sell` na classe `Stock` para incluir uma anotação. Anotações ajudam a especificar o tipo esperado do argumento, que será usado pelo decorador `@validated` para validação. Abra o arquivo `stock.py`:

```bash
code ~/project/stock.py
```

6. Modifique o método `sell` para incluir uma anotação de tipo:

```python
# stock.py

from structure import Structure
from validate import String, PositiveInteger, PositiveFloat

class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares: PositiveInteger):
        self.shares -= nshares
```

A alteração importante é adicionar `: PositiveInteger` ao parâmetro `nshares`. Isso informa ao Python (e ao nosso decorador `@validated`) para validar este argumento usando o validador `PositiveInteger`. Portanto, quando chamamos o método `sell`, o argumento `nshares` deve ser um inteiro positivo.

7. Execute os testes novamente para verificar se tudo ainda funciona. Executar testes é uma boa maneira de garantir que nossas alterações não tenham quebrado nenhuma funcionalidade existente.

```bash
cd ~/project
python3 teststock.py
```

Você deverá ver todos os testes passando:

```
.........
----------------------------------------------------------------------
Ran 9 tests in 0.001s

OK
```

8. Vamos testar nossa nova validação de argumento. Tentaremos chamar o método `sell` com argumentos válidos e inválidos para ver se a validação funciona como esperado.

```bash
cd ~/project
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); s.sell(25); print(s); try: s.sell(-25); except Exception as e: print(f'Error: {e}')"
```

Você deverá ver uma saída semelhante a:

```
Stock('GOOG', 75, 490.1)
Error: Bad Arguments
  nshares: must be >= 0
```

Isso mostra que nossa validação de argumento de método está funcionando! A primeira chamada para `sell(25)` é bem-sucedida porque `25` é um inteiro positivo. Mas a segunda chamada para `sell(-25)` falha porque `-25` não é um inteiro positivo.

Você agora implementou um sistema completo para:

1. Validar atributos de classe usando descritores. Descritores são usados para definir regras de validação para atributos de classe.
2. Coletar automaticamente informações de campo usando decoradores de classe. Decoradores de classe podem modificar o comportamento de uma classe, como coletar informações de campo.
3. Converter dados de linha em instâncias. Isso é útil ao trabalhar com dados de fontes externas.
4. Validar argumentos de método usando anotações. Anotações ajudam a especificar o tipo esperado do argumento para validação.

Isso demonstra o poder de combinar descritores e decoradores em Python para criar classes expressivas e autovalidantes.
