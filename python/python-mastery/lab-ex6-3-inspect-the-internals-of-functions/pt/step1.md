# Explorando Atributos de Funções

Em Python, as funções são consideradas objetos de primeira classe (first-class objects). O que isso significa? Bem, é semelhante a como você tem diferentes tipos de objetos no mundo real, como um livro ou uma caneta. Em Python, as funções também são objetos e, assim como outros objetos, vêm com seu próprio conjunto de atributos. Esses atributos podem nos fornecer muitas informações úteis sobre a função, como seu nome, onde ela é definida e como ela é implementada.

Vamos começar nossa exploração abrindo um shell interativo Python. Este shell é como um playground onde podemos escrever e executar código Python imediatamente. Para fazer isso, primeiro navegaremos até o diretório do projeto e, em seguida, iniciaremos o interpretador Python. Aqui estão os comandos para executar em seu terminal:

```bash
cd ~/project
python3
```

Agora que estamos no shell interativo Python, vamos definir uma função simples. Esta função pegará dois números e os somará. Veja como podemos defini-la:

```python
def add(x, y):
    'Adds two things'
    return x + y
```

Neste código, criamos uma função chamada `add`. Ela recebe dois parâmetros, `x` e `y`, e retorna sua soma. A string `'Adds two things'` é chamada de docstring, que é usada para documentar o que a função faz.

## Usando dir() para Inspecionar Atributos de Funções

Em Python, a função `dir()` é uma ferramenta útil. Ela pode ser usada para obter uma lista de todos os atributos e métodos que um objeto possui. Vamos usá-la para ver quais atributos nossa função `add` possui. Execute o seguinte código no shell interativo Python:

```python
dir(add)
```

Quando você executar este código, verá uma longa lista de atributos. Aqui está um exemplo de como a saída pode ser:

```
['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
```

Esta lista mostra todos os atributos e métodos associados à função `add`.

## Acessando Informações Básicas da Função

Agora, vamos dar uma olhada mais de perto em alguns dos atributos básicos da função. Esses atributos podem nos dizer informações importantes sobre a função. Execute o seguinte código no shell interativo Python:

```python
print(add.__name__)
print(add.__module__)
print(add.__doc__)
```

Quando você executar este código, verá a seguinte saída:

```
add
__main__
Adds two things
```

Vamos entender o que cada um desses atributos significa:

- `__name__`: Este atributo nos dá o nome da função. Em nosso caso, a função se chama `add`.
- `__module__`: Ele nos diz o módulo onde a função é definida. Quando executamos código no shell interativo, o módulo geralmente é `__main__`.
- `__doc__`: Esta é a string de documentação da função, ou docstring. Ela fornece uma breve descrição do que a função faz.

## Examinando o Código da Função

O atributo `__code__` de uma função é muito interessante. Ele contém informações sobre como a função é implementada, incluindo seu bytecode e outros detalhes. Vamos ver o que podemos aprender com ele. Execute o seguinte código no shell interativo Python:

```python
print(add.__code__.co_varnames)
print(add.__code__.co_argcount)
```

A saída será:

```
('x', 'y')
2
```

Aqui está o que esses atributos nos dizem:

- `co_varnames`: É uma tupla que contém os nomes de todas as variáveis locais usadas pela função. Em nossa função `add`, as variáveis locais são `x` e `y`.
- `co_argcount`: Este atributo nos diz o número de argumentos que a função espera. Nossa função `add` espera dois argumentos, então o valor é 2.

Se você estiver curioso para explorar mais atributos do objeto `__code__`, pode usar a função `dir()` novamente. Execute o seguinte código:

```python
dir(add.__code__)
```

Isso exibirá todos os atributos do objeto de código, que contêm detalhes de baixo nível sobre como a função é implementada.
