# Compreendendo os Fundamentos de exec()

Em Python, a função `exec()` é uma ferramenta poderosa que permite executar código criado dinamicamente em tempo de execução. Isso significa que você pode gerar código em tempo real com base em uma determinada entrada ou configuração, o que é extremamente útil em muitos cenários de programação.

Vamos começar explorando o uso básico da função `exec()`. Para fazer isso, abriremos um shell Python. Abra seu terminal e digite `python3`. Este comando iniciará o interpretador Python interativo, onde você pode executar diretamente o código Python.

```bash
python3
```

Agora, vamos definir um trecho de código Python como uma string e, em seguida, usar a função `exec()` para executá-lo. Veja como funciona:

```python
>>> code = '''
for i in range(n):
    print(i, end=' ')
'''
>>> n = 10
>>> exec(code)
0 1 2 3 4 5 6 7 8 9
```

Neste exemplo:

1. Primeiro, definimos uma string chamada `code`. Esta string contém um loop for em Python. O loop foi projetado para iterar `n` vezes e imprimir cada número de iteração.
2. Em seguida, definimos uma variável `n` e atribuímos a ela o valor 10. Esta variável é usada como o limite superior para a função `range()` em nosso loop.
3. Depois disso, chamamos a função `exec()` com a string `code` como argumento. A função `exec()` pega a string e a executa como código Python.
4. Finalmente, o loop foi executado e imprimiu os números de 0 a 9.

O verdadeiro poder da função `exec()` torna-se mais óbvio quando a usamos para criar estruturas de código mais complexas, como funções ou métodos. Vamos tentar um exemplo mais avançado onde criaremos dinamicamente um método `__init__()` para uma classe.

```python
>>> class Stock:
...     _fields = ('name', 'shares', 'price')
...
>>> argstr = ','.join(Stock._fields)
>>> code = f'def __init__(self, {argstr}):\n'
>>> for name in Stock._fields:
...     code += f'    self.{name} = {name}\n'
...
>>> print(code)
def __init__(self, name,shares,price):
    self.name = name
    self.shares = shares
    self.price = price

>>> locs = { }
>>> exec(code, locs)
>>> Stock.__init__ = locs['__init__']

>>> # Now try the class
>>> s = Stock('GOOG', 100, 490.1)
>>> s.name
'GOOG'
>>> s.shares
100
>>> s.price
490.1
```

Neste exemplo mais complexo:

1. Primeiro, definimos uma classe `Stock` com um atributo `_fields`. Este atributo é uma tupla que contém os nomes dos atributos da classe.
2. Em seguida, criamos uma string que representa o código Python para um método `__init__`. Este método é usado para inicializar os atributos do objeto.
3. Em seguida, usamos a função `exec()` para executar a string de código. Também passamos um dicionário vazio `locs` para `exec()`. A função resultante da execução é armazenada neste dicionário.
4. Depois disso, atribuímos a função armazenada no dicionário como o método `__init__` da nossa classe `Stock`.
5. Finalmente, criamos uma instância da classe `Stock` e verificamos se o método `__init__` funciona corretamente, acessando os atributos do objeto.

Este exemplo demonstra como a função `exec()` pode ser usada para criar dinamicamente métodos com base em dados disponíveis em tempo de execução.
