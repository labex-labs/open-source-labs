# Programação por Contrato (Contract Programming)

Também conhecido como Design By Contract, o uso liberal de asserções é uma abordagem para projetar software. Ele prescreve que os projetistas de software devem definir especificações de interface precisas para os componentes do software.

Por exemplo, você pode colocar asserções em todas as entradas de uma função.

```python
def add(x, y):
    assert isinstance(x, int), 'Expected int'
    assert isinstance(y, int), 'Expected int'
    return x + y
```

Verificar as entradas irá imediatamente detectar chamadores que não estão usando argumentos apropriados.

```python
>>> add(2, 3)
5
>>> add('2', '3')
Traceback (most recent call last):
...
AssertionError: Expected int
>>>
```
