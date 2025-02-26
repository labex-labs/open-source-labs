# Variables locales

Observez comment la fonction interne fait référence à des variables définies par la fonction externe.

```python
def add(x, y):
    def do_add():
        # `x` et `y` sont définis au-dessus de `add(x, y)`
        print('Adding', x, y)
        return x + y
    return do_add
```

Observez également que ces variables sont de quelque manière conservées en vie après que `add()` ait terminé.

```python
>>> a = add(3,4)
>>> a
<function do_add at 0x6a670>
>>> a()
Adding 3 4      # D'où viennent ces valeurs?
7
```
