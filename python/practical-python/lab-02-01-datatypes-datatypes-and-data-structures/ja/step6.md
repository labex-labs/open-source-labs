# タプルアンパッキング

他の場所でタプルを使用するには、その要素を変数に展開することができます。

```python
name, shares, price = s
print('Cost', shares * price)
```

左辺の変数の数は、タプルの構造と一致しなければなりません。

```python
name, shares = s     # エラー
Traceback (most recent call last):
...
ValueError: too many values to unpack
```
