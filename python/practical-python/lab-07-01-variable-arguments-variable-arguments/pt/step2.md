# Argumentos variáveis de palavra-chave (\*\*kwargs)

Uma função também pode aceitar qualquer número de argumentos de palavra-chave. Por exemplo:

```python
def f(x, y, **kwargs):
    ...
```

Chamada da função.

```python
f(2, 3, flag=True, mode='fast', header='debug')
```

As palavras-chave extras são passadas em um dicionário.

```python
def f(x, y, **kwargs):
    # x -> 2
    # y -> 3
    # kwargs -> { 'flag': True, 'mode': 'fast', 'header': 'debug' }
```
