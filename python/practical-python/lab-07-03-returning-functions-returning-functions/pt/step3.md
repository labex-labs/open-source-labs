# Closures (Fechamentos)

Quando uma função interna é retornada como resultado, essa função interna é conhecida como um _closure_ (fechamento).

```python
def add(x, y):
    # `do_add` is a closure
    def do_add():
        print('Adding', x, y)
        return x + y
    return do_add
```

_Característica essencial: Um closure retém os valores de todas as variáveis necessárias para que a função seja executada corretamente posteriormente._ Pense em um closure como uma função mais um ambiente extra que contém os valores das variáveis das quais ela depende.
