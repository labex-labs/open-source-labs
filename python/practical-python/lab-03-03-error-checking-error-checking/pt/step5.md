# Valores de Exceção (Exception Values)

Exceções têm um valor associado. Ele contém informações mais específicas sobre o que está errado.

```python
raise RuntimeError('Invalid user name')
```

Este valor faz parte da instância da exceção que é colocada na variável fornecida ao `except`.

```python
try:
    ...
except RuntimeError as e:   # `e` holds the exception raised
    ...
```

`e` é uma instância do tipo de exceção. No entanto, muitas vezes se parece com uma string quando impresso.

```python
except RuntimeError as e:
    print('Failed : Reason', e)
```
