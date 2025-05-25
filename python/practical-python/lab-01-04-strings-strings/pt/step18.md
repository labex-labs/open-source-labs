# Comentário

Ao começar a experimentar com o interpretador, você frequentemente quer saber mais sobre as operações suportadas por diferentes objetos. Por exemplo, como você descobre quais operações estão disponíveis em uma string?

Dependendo do seu ambiente Python, você pode ser capaz de ver uma lista de métodos disponíveis via preenchimento por tabulação (tab-completion). Por exemplo, tente digitar isto:

```python
>>> s = 'hello world'
>>> s.<tab key>
>>>
```

Se pressionar a tecla Tab não fizer nada, você pode recorrer à função `dir()` embutida. Por exemplo:

```python
>>> s = 'hello'
>>> dir(s)
['__add__', '__class__', '__contains__', ..., 'find', 'format',
'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace',
'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition',
'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit',
'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase',
'title', 'translate', 'upper', 'zfill']
>>>
```

`dir()` produz uma lista de todas as operações que podem aparecer após o `(.)`. Use o comando `help()` para obter mais informações sobre uma operação específica:

```python
>>> help(s.upper)
Help on built-in function upper:

upper(...)
    S.upper() -> string

    Return a copy of the string S converted to uppercase.
>>>
```
