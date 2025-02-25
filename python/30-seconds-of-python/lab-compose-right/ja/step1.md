# 逆合成関数

1つ以上の関数を引数として受け取り、左から右への関数合成を行う新しい関数を返す`compose_right`関数を作成します。最初の（最も左の）関数は1つ以上の引数を受け取ることができます。残りの関数は単項関数でなければなりません。

あなたの実装は、左から右への関数合成を行うために`functools`モジュールの`reduce`関数を使用する必要があります。

```python
from functools import reduce

def compose_right(*fns):
  # ここにコードを記述してください
```

```python
from functools import reduce

def compose_right(*fns):
  return reduce(lambda f, g: lambda *args: g(f(*args)), fns)
```

```python
add = lambda x, y: x + y
square = lambda x: x * x
add_and_square = compose_right(add, square)
add_and_square(1, 2) # 9
```
