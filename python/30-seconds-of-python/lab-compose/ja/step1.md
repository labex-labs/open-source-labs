# 関数を合成する

`compose(*fns)` という名前の関数を書きます。この関数は、1つ以上の関数を引数として受け取り、入力関数を右から左に合成した結果である新しい関数を返します。最後の（最も右の）関数は1つ以上の引数を受け取ることができます。残りの関数は単項関数でなければなりません。

```python
from functools import reduce

def compose(*fns):
  return reduce(lambda f, g: lambda *args: f(g(*args)), fns)
```

```python
add5 = lambda x: x + 5
multiply = lambda x, y: x * y
multiply_and_add_5 = compose(add5, multiply)
multiply_and_add_5(5, 2) # 15
```
