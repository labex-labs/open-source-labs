# Decoradores

Colocar _wrappers_ (envoltórios) em torno de funções é extremamente comum em Python. Tão comum que existe uma sintaxe especial para isso.

```python
def add(x, y):
    return x + y
add = logged(add)

# Sintaxe especial
@logged
def add(x, y):
    return x + y
```

A sintaxe especial executa exatamente as mesmas etapas mostradas acima. Um decorador é apenas uma nova sintaxe. Diz-se que ele _decora_ a função.
