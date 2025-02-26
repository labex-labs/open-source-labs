# キーワード引数の可変長引数 (\*\*kwargs)

関数は、任意の数のキーワード引数を受け付けることもできます。たとえば：

```python
def f(x, y, **kwargs):
  ...
```

関数呼び出し。

```python
f(2, 3, flag=True, mode='fast', header='debug')
```

追加のキーワードは辞書で渡されます。

```python
def f(x, y, **kwargs):
    # x -> 2
    # y -> 3
    # kwargs -> { 'flag': True,'mode': 'fast', 'header': 'debug' }
```
