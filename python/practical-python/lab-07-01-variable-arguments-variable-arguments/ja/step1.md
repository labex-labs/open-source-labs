# 位置引数の可変長引数 (\*args)

任意の数の引数を受け付ける関数は、可変長引数を使用すると言われます。たとえば：

```python
def f(x, *args):
   ...
```

関数呼び出し。

```python
f(1,2,3,4,5)
```

追加の引数はタプルとして渡されます。

```python
def f(x, *args):
    # x -> 1
    # args -> (2,3,4,5)
```
