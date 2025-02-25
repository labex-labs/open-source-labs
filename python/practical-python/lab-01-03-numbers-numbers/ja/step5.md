# 比較

以下の比較演算子 / 関係演算子は数値と共に使用できます。

    x < y      未満
    x <= y     未満または等しい
    x > y      大きい
    x >= y     大きいまたは等しい
    x == y     等しい
    x!= y     等しくない

`and`、`or`、`not` を使用して、より複雑なブール式を作成できます。

以下はいくつかの例です。

```python
if b >= a and b <= c:
    print('b is between a and c')

if not (b < a or b > c):
    print('b is still between a and c')
```
