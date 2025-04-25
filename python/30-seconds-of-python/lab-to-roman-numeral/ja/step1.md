# 整数をローマ数字に変換する

1 から 3999（両方とも含む）の整数 `num` を受け取り、そのローマ数字表記を文字列として返す関数 `to_roman_numeral(num)` を作成します。

整数をそのローマ数字表記に変換するには、(ローマ数字の値，整数) の形式のタプルが含まれるルックアップリストを使用できます。その後、`for` ループを使用してルックアップリストの値を反復処理し、`divmod()` を使用して余りで `num` を更新し、結果にローマ数字表記を追加します。

関数は、入力整数のローマ数字表記を返す必要があります。

```python
def to_roman_numeral(num):
  lookup = [
    (1000, 'M'),
    (900, 'CM'),
    (500, 'D'),
    (400, 'CD'),
    (100, 'C'),
    (90, 'XC'),
    (50, 'L'),
    (40, 'XL'),
    (10, 'X'),
    (9, 'IX'),
    (5, 'V'),
    (4, 'IV'),
    (1, 'I'),
  ]
  res = ''
  for (n, roman) in lookup:
    (d, num) = divmod(num, n)
    res += roman * d
  return res
```

```python
to_roman_numeral(3) # 'III'
to_roman_numeral(11) # 'XI'
to_roman_numeral(1998) # 'MCMXCVIII'
```
