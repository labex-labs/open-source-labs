# はじめに

次の関数を考えてみましょう。

```python
def add(x, y):
    def do_add():
        print('Adding', x, y)
        return x + y
    return do_add
```

これは、別の関数を返す関数です。

```python
>>> a = add(3,4)
>>> a
<function add.<locals>.do_add at 0x7f27d8a38790>
>>> a()
Adding 3 4
7
```
