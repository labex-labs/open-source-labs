# Variables locales

Observe cómo la función interna se refiere a las variables definidas por la función externa.

```python
def add(x, y):
    def do_add():
        # `x` y `y` se definen arriba de `add(x, y)`
        print('Adding', x, y)
        return x + y
    return do_add
```

Observe además que esas variables siguen existiendo de alguna manera después de que `add()` haya terminado.

```python
>>> a = add(3,4)
>>> a
<function do_add at 0x6a670>
>>> a()
Adding 3 4      # ¿De dónde provienen estos valores?
7
```
