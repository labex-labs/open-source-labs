# Construindo um Decorador de Validação

Nesta etapa, vamos criar um decorador mais prático. Um decorador em Python é um tipo especial de função que pode modificar o comportamento de outra função. O decorador que criaremos validará os argumentos da função com base nas anotações de tipo. Anotações de tipo são uma maneira de especificar os tipos de dados esperados dos argumentos e do valor de retorno de uma função. Este é um caso de uso comum em aplicações do mundo real porque ajuda a garantir que as funções recebam os tipos de entrada corretos, o que pode evitar muitos bugs.

## Entendendo as Classes de Validação

Já criamos um arquivo chamado `validate.py` para você, e ele contém algumas classes de validação. Classes de validação são usadas para verificar se um valor atende a certos critérios. Para ver o que está dentro deste arquivo, você precisa abri-lo no editor VSCode. Você pode fazer isso executando os seguintes comandos no terminal:

```bash
cd /home/labex/project
code validate.py
```

O arquivo tem três classes:

1. `Validator` - Esta é uma classe base. Uma classe base fornece uma estrutura geral que outras classes podem herdar. Neste caso, ela fornece a estrutura básica para validação.
2. `Integer` - Esta classe de validador é usada para garantir que um valor seja um inteiro. Se você passar um valor não inteiro para uma função que usa este validador, ele gerará um erro.
3. `PositiveInteger` - Esta classe de validador garante que um valor seja um inteiro positivo. Portanto, se você passar um inteiro negativo ou zero, ele também gerará um erro.

## Adicionando o Decorador de Validação

Agora, vamos adicionar uma função decoradora chamada `validated` ao arquivo `validate.py`. Este decorador executará várias tarefas importantes:

1. Ele inspecionará as anotações de tipo de uma função. Anotações de tipo são como pequenas notas que nos dizem que tipo de dados a função espera.
2. Ele validará os argumentos passados para a função em relação a essas anotações de tipo. Isso significa que ele verificará se os valores passados para a função são do tipo correto.
3. Ele também validará o valor de retorno da função em relação à sua anotação. Portanto, ele garante que a função retorne o tipo de dados que deveria.
4. Se a validação falhar, ele gerará mensagens de erro informativas. Essas mensagens dirão exatamente o que deu errado, como qual argumento tinha o tipo errado.

Adicione o seguinte código ao final do arquivo `validate.py`:

```python
# Add to validate.py

import inspect
import functools

def validated(func):
    sig = inspect.signature(func)

    print(f'Validating {func.__name__} {sig}')

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Bind arguments to the signature
        bound = sig.bind(*args, **kwargs)
        errors = []

        # Validate each argument
        for name, value in bound.arguments.items():
            if name in sig.parameters:
                param = sig.parameters[name]
                if param.annotation != inspect.Parameter.empty:
                    try:
                        # Create an instance of the validator and validate the value
                        if isinstance(param.annotation, type) and issubclass(param.annotation, Validator):
                            validator = param.annotation()
                            bound.arguments[name] = validator.validate(value)
                    except Exception as e:
                        errors.append(f'    {name}: {e}')

        # If validation errors, raise an exception
        if errors:
            raise TypeError('Bad Arguments\n' + '\n'.join(errors))

        # Call the function
        result = func(*bound.args, **bound.kwargs)

        # Validate the return value
        if sig.return_annotation != inspect.Signature.empty:
            try:
                if isinstance(sig.return_annotation, type) and issubclass(sig.return_annotation, Validator):
                    validator = sig.return_annotation()
                    result = validator.validate(result)
            except Exception as e:
                raise TypeError(f'Bad return: {e}') from None

        return result

    return wrapper
```

Este código usa o módulo `inspect` do Python. O módulo `inspect` nos permite obter informações sobre objetos ativos, como funções. Aqui, o usamos para examinar a assinatura da função e validar argumentos com base nas anotações de tipo. Também usamos `functools.wraps`. Esta é uma função auxiliar que preserva os metadados da função original, como seu nome e docstring. Metadados são como informações extras sobre a função que nos ajudam a entender o que ela faz.

## Testando o Decorador de Validação

Vamos criar um arquivo para testar nosso decorador de validação. Criaremos um novo arquivo chamado `test_validate.py` e adicionaremos o seguinte código a ele:

```python
# test_validate.py

from validate import Integer, PositiveInteger, validated

@validated
def add(x: Integer, y: Integer) -> Integer:
    return x + y

@validated
def pow(x: Integer, y: Integer) -> Integer:
    return x ** y

# Test with a class
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price

    @validated
    def sell(self, nshares: PositiveInteger):
        self.shares -= nshares
```

Agora, testaremos nosso decorador no interpretador Python. Primeiro, navegue até o diretório do projeto e inicie o interpretador Python executando estes comandos no terminal:

```bash
cd /home/labex/project
python3
```

Em seguida, no interpretador Python, podemos executar o seguinte código para testar nosso decorador:

```python
>>> from test_validate import add, pow, Stock
Validating add (x: validate.Integer, y: validate.Integer) -> validate.Integer
Validating pow (x: validate.Integer, y: validate.Integer) -> validate.Integer
Validating sell (self, nshares: validate.PositiveInteger) -> <class 'inspect._empty'>
>>>
>>> # Test with valid inputs
>>> add(2, 3)
5
>>>
>>> # Test with invalid inputs
>>> add('2', '3')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/labex/project/validate.py", line 75, in wrapper
    raise TypeError('Bad Arguments\n' + '\n'.join(errors))
TypeError: Bad Arguments
    x: Expected <class 'int'>
    y: Expected <class 'int'>
>>>
>>> # Test valid power
>>> pow(2, 3)
8
>>>
>>> # Test with negative exponent (produces non - integer result)
>>> pow(2, -1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/labex/project/validate.py", line 83, in wrapper
    raise TypeError(f'Bad return: {e}') from None
TypeError: Bad return: Expected <class 'int'>
>>>
>>> # Test with a class
>>> s = Stock("GOOG", 100, 490.1)
>>> s.sell(50)
>>> s.shares
50
>>>
>>> # Test with invalid shares
>>> s.sell(-10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/labex/project/validate.py", line 75, in wrapper
    raise TypeError('Bad Arguments\n' + '\n'.join(errors))
TypeError: Bad Arguments
    nshares: Expected value > 0
>>> exit()
```

Como você pode ver, nosso decorador `validated` impôs com sucesso a verificação de tipo nos argumentos da função e nos valores de retorno. Isso é muito útil porque torna nosso código mais robusto. Em vez de deixar erros de tipo se propagarem mais profundamente no código e causar bugs difíceis de encontrar, nós os capturamos nos limites da função.
