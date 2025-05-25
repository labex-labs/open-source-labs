# Combinando ambos

Uma função também pode aceitar qualquer número de argumentos variáveis de palavra-chave e não-palavra-chave.

```python
def f(*args, **kwargs):
    ...
```

Chamada da função.

```python
f(2, 3, flag=True, mode='fast', header='debug')
```

Os argumentos são separados em componentes posicionais e de palavra-chave.

```python
def f(*args, **kwargs):
    # args = (2, 3)
    # kwargs -> { 'flag': True, 'mode': 'fast', 'header': 'debug' }
    ...
```

Esta função aceita qualquer combinação de argumentos posicionais ou de palavra-chave. É, por vezes, utilizada ao escrever wrappers ou quando se pretende passar argumentos para outra função.
