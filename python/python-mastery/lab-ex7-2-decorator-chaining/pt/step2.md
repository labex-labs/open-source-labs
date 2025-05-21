# Criando Decoradores com Argumentos

Até agora, temos usado o _decorator_ `@logged`, que sempre imprime uma mensagem fixa. Mas e se você quiser personalizar o formato da mensagem? Nesta seção, aprenderemos como criar um novo _decorator_ que pode aceitar argumentos, dando a você mais flexibilidade na forma como você usa _decorators_.

## Entendendo Decoradores Parametrizados

Um _decorator_ parametrizado é um tipo especial de função. Em vez de modificar diretamente outra função, ele retorna um _decorator_. A estrutura geral de um _decorator_ parametrizado se parece com isto:

```python
def decorator_with_args(arg1, arg2, ...):
    def actual_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Use arg1, arg2, ... here
            # Call the original function
            return func(*args, **kwargs)
        return wrapper
    return actual_decorator
```

Quando você usa `@decorator_with_args(value1, value2)` em seu código, o Python primeiro chama `decorator_with_args(value1, value2)`. Essa chamada retorna o _decorator_ real, que é então aplicado à função que segue a sintaxe `@`. Esse processo de duas etapas é fundamental para o funcionamento dos _decorators_ parametrizados.

## Criando o Decorator logformat

Vamos criar um _decorator_ `@logformat(fmt)` que recebe uma string de formato como argumento. Isso nos permitirá personalizar a mensagem de _logging_.

1. Abra `logcall.py` no WebIDE e adicione o novo _decorator_. O código abaixo mostra como definir tanto o _decorator_ `logged` existente quanto o novo _decorator_ `logformat`:

```python
from functools import wraps

def logged(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

def logformat(fmt):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(fmt.format(func=func))
            return func(*args, **kwargs)
        return wrapper
    return decorator
```

No _decorator_ `logformat`, a função externa `logformat` recebe uma string de formato `fmt` como argumento. Em seguida, ele retorna a função `decorator`, que é o _decorator_ real que modifica a função de destino.

2. Agora, vamos testar nosso novo _decorator_ modificando `sample.py`. O código a seguir mostra como usar os _decorators_ `logged` e `logformat` em diferentes funções:

```python
from logcall import logged, logformat

@logged
def add(x, y):
    "Adds two numbers"
    return x + y

@logged
def sub(x, y):
    "Subtracts y from x"
    return x - y

@logformat('{func.__code__.co_filename}:{func.__name__}')
def mul(x, y):
    "Multiplies two numbers"
    return x * y
```

Aqui, as funções `add` e `sub` usam o _decorator_ `logged`, enquanto a função `mul` usa o _decorator_ `logformat` com uma string de formato personalizada.

3. Execute o `sample.py` atualizado para ver os resultados. Abra seu terminal e execute o seguinte comando:

```bash
cd ~/project
python3 -c "import sample; print(sample.add(2, 3)); print(sample.mul(2, 3))"
```

Você deve ver uma saída semelhante a:

```
Calling add
5
sample.py:mul
6
```

Essa saída mostra que o _decorator_ `logged` imprime o nome da função como esperado, e o _decorator_ `logformat` usa a string de formato personalizada para imprimir o nome do arquivo e o nome da função.

## Redefinindo o Decorator logged Usando logformat

Agora que temos um _decorator_ `logformat` mais flexível, podemos redefinir nosso _decorator_ `logged` original usando-o. Isso nos ajudará a reutilizar o código e manter um formato de _logging_ consistente.

1. Atualize `logcall.py` com o seguinte código:

```python
from functools import wraps

def logformat(fmt):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(fmt.format(func=func))
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Define logged using logformat
logged = lambda func: logformat("Calling {func.__name__}")(func)
```

Aqui, usamos uma função lambda para definir o _decorator_ `logged` em termos do _decorator_ `logformat`. A função lambda recebe uma função `func` e aplica o _decorator_ `logformat` com uma string de formato específica.

2. Teste se o _decorator_ `logged` redefinido ainda funciona. Abra seu terminal e execute o seguinte comando:

```bash
cd ~/project
python3 -c "from logcall import logged; @logged
def greet(name):
    return f'Hello, {name}'
    
print(greet('World'))"
```

Você deve ver:

```
Calling greet
Hello, World
```

Isso mostra que o _decorator_ `logged` redefinido funciona como esperado, e reutilizamos com sucesso o _decorator_ `logformat` para obter um formato de _logging_ consistente.
