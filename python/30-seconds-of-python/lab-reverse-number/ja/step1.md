# 数値を逆順にする

引数として数値を受け取り、その数値の逆順を返す関数 `reverse_number(n)` を作成します。この関数は以下の要件を満たす必要があります。

- 関数は、数値が正であろうと負であろうと、数値を逆順にする必要があります。
- 入力が浮動小数点数の場合、関数は浮動小数点数を返し、入力が整数の場合、整数を返す必要があります。
- 関数は、数値を直接逆順にする組み込み関数（例えば `reversed()`）を使用してはいけません。
- 関数は、数値を直接文字列に変換する組み込み関数（例えば `str()`）を使用してはいけません。
- 関数は、文字列から数値を直接変換する組み込み関数（例えば `int()` または `float()`）を使用してはいけません。

```python
from math import copysign

def reverse_number(n):
  return copysign(float(str(n)[::-1].replace('-', '')), n)
```

```python
reverse_number(981) # 189
reverse_number(-500) # -5
reverse_number(73.6) # 6.37
reverse_number(-5.23) # -32.5
```
