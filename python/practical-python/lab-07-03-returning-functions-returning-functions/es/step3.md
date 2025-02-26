# Cerraduras

Cuando una función interna se devuelve como resultado, esa función interna se conoce como una _cerradura_.

```python
def add(x, y):
    # `do_add` es una cerradura
    def do_add():
        print('Adding', x, y)
        return x + y
    return do_add
```

_Característica esencial: Una cerradura retiene los valores de todas las variables necesarias para que la función funcione correctamente más adelante._ Piense en una cerradura como una función más un entorno adicional que contiene los valores de las variables en las que depende.
