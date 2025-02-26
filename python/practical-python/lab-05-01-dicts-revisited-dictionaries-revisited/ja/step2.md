# 辞書とモジュール

モジュール内では、辞書がすべてのグローバル変数と関数を保持します。

```python
# foo.py

x = 42
def bar():
  ...

def spam():
  ...
```

`foo.__dict__` または `globals()` を調べると、辞書が見えます。

```python
{
    'x' : 42,
    'bar' : <function bar>,
   'spam' : <function spam>
}
```
