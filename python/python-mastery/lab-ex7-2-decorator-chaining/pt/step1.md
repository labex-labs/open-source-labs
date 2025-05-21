# Preservando Metadados de Funções em Decoradores

Em Python, _decorators_ (decoradores) são uma ferramenta poderosa que permite modificar o comportamento de funções. No entanto, ao usar um _decorator_ para envolver uma função, há um pequeno problema. Por padrão, os metadados da função original, como seu nome, _docstring_ (string de documentação) e anotações, são perdidos. Metadados são importantes porque ajudam na introspecção (examinando a estrutura do código) e na geração de documentação. Vamos primeiro verificar esse problema.

Abra seu terminal no WebIDE. Executaremos alguns comandos Python para ver o que acontece quando usamos um _decorator_. Os seguintes comandos criarão uma função simples `add` envolvida com um _decorator_ e, em seguida, imprimirão a função e sua _docstring_.

```bash
cd ~/project
python3 -c "from logcall import logged; @logged
def add(x,y):
    'Adds two things'
    return x+y
    
print(add)
print(add.__doc__)"
```

Ao executar esses comandos, você verá uma saída semelhante a esta:

```
<function wrapper at 0x...>
None
```

Observe que, em vez de mostrar o nome da função como `add`, ele mostra `wrapper`. E a _docstring_, que deveria ser `'Adds two things'`, é `None`. Isso pode ser um grande problema quando você está usando ferramentas que dependem desses metadados, como ferramentas de introspecção ou geradores de documentação.

## Corrigindo o Problema com functools.wraps

O módulo `functools` do Python vem para o resgate. Ele fornece um _decorator_ `wraps` que pode nos ajudar a preservar os metadados da função. Vamos ver como podemos modificar nosso _decorator_ `logged` para usar `wraps`.

1. Primeiro, abra o arquivo `logcall.py` no WebIDE. Você pode navegar até o diretório do projeto usando o seguinte comando no terminal:

```bash
cd ~/project
```

2. Agora, atualize o _decorator_ `logged` em `logcall.py` com o seguinte código. O _decorator_ `@wraps(func)` é a chave aqui. Ele copia todos os metadados da função original `func` para a função _wrapper_.

```python
from functools import wraps

def logged(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper
```

3. O _decorator_ `@wraps(func)` faz um trabalho importante. Ele pega todos os metadados (como o nome, _docstring_ e anotações) da função original `func` e os anexa à função `wrapper`. Dessa forma, quando usamos a função decorada, ela terá os metadados corretos.

4. Vamos testar nosso _decorator_ aprimorado. Execute os seguintes comandos no terminal:

```bash
python3 -c "from logcall import logged; @logged
def add(x,y):
    'Adds two things'
    return x+y
    
print(add)
print(add.__doc__)"
```

Agora você deve ver:

```
<function add at 0x...>
Adds two things
```

Ótimo! O nome da função e a _docstring_ são preservados. Isso significa que nosso _decorator_ agora está funcionando como esperado, e os metadados da função original estão intactos.

## Corrigindo o Decorator validate.py

Agora, vamos aplicar a mesma correção ao _decorator_ `validated` em `validate.py`. Este _decorator_ é usado para validar os tipos de argumentos de função e o valor de retorno com base nas anotações da função.

1. Abra `validate.py` no WebIDE.

2. Atualize o _decorator_ `validated` com o _decorator_ `@wraps`. O seguinte código mostra como fazer isso. O _decorator_ `@wraps(func)` é adicionado à função `wrapper` dentro do _decorator_ `validated` para preservar os metadados.

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
```

3. Vamos testar se nosso _decorator_ `validated` agora preserva metadados. Execute os seguintes comandos no terminal:

```bash
python3 -c "from validate import validated, Integer; @validated
def multiply(x: Integer, y: Integer) -> Integer:
    'Multiplies two integers'
    return x * y
    
print(multiply)
print(multiply.__doc__)"
```

Você deve ver:

```
<function multiply at 0......>
Multiplies two integers
```

Agora, ambos os _decorators_, `logged` e `validated`, preservam adequadamente os metadados das funções que decoram. Isso garante que, ao usar esses _decorators_, as funções ainda terão seus nomes originais, _docstrings_ e anotações, o que é muito útil para a legibilidade e manutenibilidade do código.
