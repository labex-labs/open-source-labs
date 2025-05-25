# Variáveis Locais

Observe como a função interna se refere a variáveis definidas pela função externa.

```python
def add(x, y):
    def do_add():
        # `x` and `y` are defined above `add(x, y)`
        print('Adding', x, y)
        return x + y
    return do_add
```

Observe ainda que essas variáveis são de alguma forma mantidas ativas após a conclusão de `add()`.

```python
>>> a = add(3,4)
>>> a
<function do_add at 0x6a670>
>>> a()
Adding 3 4      # Where are these values coming from?
7
```
