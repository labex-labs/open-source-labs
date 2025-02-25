# カリング関数

与えられた関数`fn`をカリングする関数`curry(fn, *args)`を書きます。この関数は、与えられた引数`args`が部分的に適用された状態で`fn`と同じように振る舞う新しい関数を返す必要があります。

```python
from functools import partial

def curry(fn, *args):
  return partial(fn, *args)
```

```python
add = lambda x, y: x + y
add10 = curry(add, 10)
add10(20) # 30
```
