# 両方を組み合わせる

関数は、任意の数の可変長キーワード引数と非キーワード引数を受け付けることもできます。

```python
def f(*args, **kwargs):
 ...
```

関数呼び出し。

```python
f(2, 3, flag=True, mode='fast', header='debug')
```

引数は位置引数とキーワード引数に分けられます。

```python
def f(*args, **kwargs):
    # args = (2, 3)
    # kwargs -> { 'flag': True,'mode': 'fast', 'header': 'debug' }
 ...
```

この関数は、位置引数またはキーワード引数の任意の組み合わせを受け取ります。これは、ラッパーを書くときや、別の関数に引数を渡したいときに使用されることがあります。
