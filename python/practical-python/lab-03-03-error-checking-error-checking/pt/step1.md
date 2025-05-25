# Como os programas falham

Python não realiza nenhuma verificação ou validação dos tipos ou valores dos argumentos de função. Uma função funcionará em quaisquer dados que sejam compatíveis com as instruções na função.

```python
def add(x, y):
    return x + y

add(3, 4)               # 7
add('Hello', 'World')   # 'HelloWorld'
add('3', '4')           # '34'
```

Se houver erros em uma função, eles aparecem em tempo de execução (como uma exceção).

```python
def add(x, y):
    return x + y

>>> add(3, '4')
Traceback (most recent call last):
...
TypeError: unsupported operand type(s) for +:
'int' and 'str'
>>>
```

Para verificar o código, há uma forte ênfase em testes (abordados posteriormente).
