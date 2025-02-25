# 階乗

非負整数 `num` を引数として受け取り、その階乗を返す関数 `factorial(num)` を書きます。この関数は再帰を使って階乗を計算する必要があります。`num` が `1` 以下の場合、`1` を返します。それ以外の場合、`num` と `num - 1` の階乗の積を返します。`num` が負または浮動小数点数の場合、関数は例外を投げる必要があります。

```python
def factorial(num):
  if not ((num >= 0) and (num % 1 == 0)):
    raise Exception("Number can't be floating point or negative.")
  return 1 if num == 0 else num * factorial(num - 1)
```

```python
factorial(6) # 720
```
