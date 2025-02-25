# 中央値

`find_median` という名前のPython関数を書きましょう。この関数は、数値のリストを引数として受け取り、そのリストの中央値を返します。あなたの関数は次の手順を実行する必要があります。

1. `list.sort()` を使用してリストの数値をソートします。
2. 中央値を見つけます。リストの長さが奇数の場合、中央値はリストの真ん中の要素であり、リストの長さが偶数の場合、中央値は真ん中の2つの要素の平均です。
3. 中央値を返します。

あなたの関数は、直接問題を解く組み込みのPythonライブラリや関数を使用してはいけません。

```python
def median(list):
  list.sort()
  list_length = len(list)
  if list_length % 2 == 0:
    return (list[int(list_length / 2) - 1] + list[int(list_length / 2)]) / 2
  return float(list[int(list_length / 2)])
```

```python
median([1, 2, 3]) # 2.0
median([1, 2, 3, 4]) # 2.5
```
