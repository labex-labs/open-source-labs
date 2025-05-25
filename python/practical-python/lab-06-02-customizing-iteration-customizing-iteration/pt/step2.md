# Geradores (Generators)

Um gerador (generator) é uma função que define a iteração.

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1
```

Por exemplo:

```python
>>> for x in countdown(10):
...   print(x, end=' ')
...
10 9 8 7 6 5 4 3 2 1
>>>
```

Um gerador (generator) é qualquer função que usa a instrução `yield`.

O comportamento dos geradores (generators) é diferente de uma função normal. Chamar uma função geradora (generator function) cria um objeto gerador (generator object). Ele não executa a função imediatamente.

```python
def countdown(n):
    # Added a print statement
    print('Counting down from', n)
    while n > 0:
        yield n
        n -= 1
```

```python
>>> x = countdown(10)
# There is NO PRINT STATEMENT
>>> x
# x is a generator object
<generator object at 0x58490>
>>>
```

A função só executa na chamada `__next__()`.

```python
>>> x = countdown(10)
>>> x
<generator object at 0x58490>
>>> x.__next__()
Counting down from 10
10
>>>
```

`yield` produz um valor, mas suspende a execução da função. A função é retomada na próxima chamada para `__next__()`.

```python
>>> x.__next__()
9
>>> x.__next__()
8
```

Quando o gerador (generator) finalmente retorna, a iteração levanta um erro.

```python
>>> x.__next__()
1
>>> x.__next__()
Traceback (most recent call last):
File "<stdin>", line 1, in ? StopIteration
>>>
```

_Observação: Uma função geradora (generator function) implementa o mesmo protocolo de baixo nível que as instruções for usam em listas, tuplas, dicionários, arquivos, etc._
