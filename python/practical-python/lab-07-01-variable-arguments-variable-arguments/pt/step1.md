# Argumentos posicionais variáveis (\*args)

Uma função que aceita _qualquer número_ de argumentos diz-se que utiliza argumentos variáveis. Por exemplo:

```python
def f(x, *args):
    ...
```

Chamada da função.

```python
f(1,2,3,4,5)
```

Os argumentos extras são passados como uma tupla.

```python
def f(x, *args):
    # x -> 1
    # args -> (2,3,4,5)
```
