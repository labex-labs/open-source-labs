# 逆合成関数

## 問題

1 つ以上の関数を引数として受け取り、左から右への関数合成を行う新しい関数を返す`compose_right`関数を書きなさい。最初の（最も左の）関数は 1 つ以上の引数を受け取ることができます。残りの関数は単項関数でなければなりません。

あなたの実装は、左から右への関数合成を行うために`functools`モジュールの`reduce`関数を使用する必要があります。

```python
from functools import reduce

def compose_right(*fns):
  # ここにコードを記述してください
```

## 例

```python
add = lambda x, y: x + y
square = lambda x: x * x
add_and_square = compose_right(add, square)
assert add_and_square(1, 2) == 9
```

上記の例では、2 つの関数`add`と`square`を定義しています。その後、`compose_right`関数を使用して、最初に 2 つの数を加算し、その結果を 2 乗する新しい関数`add_and_square`を作成します。その後、`add_and_square`関数に引数`1`と`2`を渡して呼び出し、結果として`9`が返されます。
