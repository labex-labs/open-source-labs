# Criando um Decorator de Aplicação de Tipos com Argumentos

Nos passos anteriores, aprendemos sobre o _decorator_ `@validated`. Este _decorator_ é usado para impor anotações de tipo em funções Python. Anotações de tipo são uma maneira de especificar os tipos esperados de argumentos de função e valores de retorno. Agora, vamos dar um passo adiante. Criaremos um _decorator_ mais flexível que pode aceitar especificações de tipo como argumentos. Isso significa que podemos definir os tipos que queremos para cada argumento e o valor de retorno de uma forma mais explícita.

## Entendendo o Objetivo

Nosso objetivo é criar um _decorator_ `@enforce()`. Este _decorator_ nos permitirá especificar restrições de tipo usando argumentos de palavra-chave. Aqui está um exemplo de como ele funcionará:

```python
@enforce(x=Integer, y=Integer, return_=Integer)
def add(x, y):
    return x + y
```

Neste exemplo, estamos usando o _decorator_ `@enforce` para especificar que os argumentos `x` e `y` da função `add` devem ser do tipo `Integer`, e o valor de retorno também deve ser do tipo `Integer`. Este _decorator_ se comportará de maneira semelhante ao nosso _decorator_ `@validated` anterior, mas nos dá mais controle sobre as especificações de tipo.

## Criando o Decorator enforce

1. Primeiro, abra o arquivo `validate.py` no WebIDE. Adicionaremos nosso novo _decorator_ a este arquivo. Aqui está o código que adicionaremos:

```python
from functools import wraps

class Integer:
    @classmethod
    def __instancecheck__(cls, x):
        return isinstance(x, int)

def validated(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Get function annotations
        annotations = func.__annotations__
        # Check arguments against annotations
        for arg_name, arg_value in zip(func.__code__.co_varnames, args):
            if arg_name in annotations and not isinstance(arg_value, annotations[arg_name]):
                raise TypeError(f'Expected {arg_name} to be {annotations[arg_name].__name__}')

        # Run the function and get the result
        result = func(*args, **kwargs)

        # Check the return value
        if 'return' in annotations and not isinstance(result, annotations['return']):
            raise TypeError(f'Expected return value to be {annotations["return"].__name__}')

        return result
    return wrapper

def enforce(**type_specs):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Check argument types
            for arg_name, arg_value in zip(func.__code__.co_varnames, args):
                if arg_name in type_specs and not isinstance(arg_value, type_specs[arg_name]):
                    raise TypeError(f'Expected {arg_name} to be {type_specs[arg_name].__name__}')

            # Run the function and get the result
            result = func(*args, **kwargs)

            # Check the return value
            if 'return_' in type_specs and not isinstance(result, type_specs['return_']):
                raise TypeError(f'Expected return value to be {type_specs["return_"].__name__}')

            return result
        return wrapper
    return decorator
```

Vamos detalhar o que este código faz. A classe `Integer` é usada para definir um tipo personalizado. O _decorator_ `validated` verifica os tipos de argumentos de função e o valor de retorno com base nas anotações de tipo da função. O _decorator_ `enforce` é o novo que estamos criando. Ele recebe argumentos de palavra-chave que especificam os tipos para cada argumento e o valor de retorno. Dentro da função `wrapper` do _decorator_ `enforce`, verificamos se os tipos dos argumentos e o valor de retorno correspondem aos tipos especificados. Caso contrário, lançamos um `TypeError`.

2. Agora, vamos testar nosso novo _decorator_ `@enforce`. Executaremos alguns casos de teste para ver se ele funciona como esperado. Aqui está o código para executar os testes:

```bash
cd ~/project
python3 -c "from validate import enforce, Integer

@enforce(x=Integer, y=Integer, return_=Integer)
def add(x, y):
    return x + y

# This should work
print(add(2, 3))

# This should raise a TypeError
try:
    print(add('2', 3))
except TypeError as e:
    print(f'Error: {e}')

# This should raise a TypeError
try:
    @enforce(x=Integer, y=Integer, return_=Integer)
    def bad_add(x, y):
        return str(x + y)
    print(bad_add(2, 3))
except TypeError as e:
    print(f'Error: {e}')"
```

Neste código de teste, primeiro definimos uma função `add` com o _decorator_ `@enforce`. Em seguida, chamamos a função `add` com argumentos válidos, que devem funcionar sem erros. Em seguida, chamamos a função `add` com um argumento inválido, que deve lançar um `TypeError`. Finalmente, definimos uma função `bad_add` que retorna um valor do tipo errado, que também deve lançar um `TypeError`.

Ao executar este código de teste, você deve ver uma saída semelhante à seguinte:

```
5
Error: Expected x to be Integer
Error: Expected return value to be Integer
```

Esta saída mostra que nosso _decorator_ `@enforce` está funcionando corretamente. Ele lança um `TypeError` quando os tipos dos argumentos ou o valor de retorno não correspondem aos tipos especificados.

## Comparando as Duas Abordagens

Tanto o _decorator_ `@validated` quanto o `@enforce` atingem o mesmo objetivo de impor restrições de tipo, mas o fazem de maneiras diferentes.

1. O _decorator_ `@validated` usa as anotações de tipo embutidas do Python. Aqui está um exemplo:

   ```python
   @validated
   def add(x: Integer, y: Integer) -> Integer:
       return x + y
   ```

   Com esta abordagem, especificamos os tipos diretamente na definição da função usando anotações de tipo. Este é um recurso embutido do Python, e ele fornece melhor suporte em Ambientes de Desenvolvimento Integrados (IDEs). Os IDEs podem usar essas anotações de tipo para fornecer preenchimento de código, verificação de tipo e outros recursos úteis.

2. O _decorator_ `@enforce`, por outro lado, usa argumentos de palavra-chave para especificar os tipos. Aqui está um exemplo:

   ```python
   @enforce(x=Integer, y=Integer, return_=Integer)
   def add(x, y):
       return x + y
   ```

   Esta abordagem é mais explícita porque estamos passando diretamente as especificações de tipo como argumentos para o _decorator_. Pode ser útil ao trabalhar com bibliotecas que dependem de outros sistemas de anotação.

Cada abordagem tem suas próprias vantagens. As anotações de tipo são uma parte nativa do Python e oferecem melhor suporte de IDE, enquanto a abordagem `@enforce` nos dá mais flexibilidade e explicitude. Você pode escolher a abordagem que melhor se adapta às suas necessidades, dependendo do projeto em que está trabalhando.
