# zip() 関数

`zip` 関数は複数のシーケンスを取り、それらを結合するイテレータを作成します。

```python
columns = ['name','shares', 'price']
values = ['GOOG', 100, 490.1 ]
pairs = zip(columns, values)
# ('name', 'GOOG'), ('shares',100), ('price',490.1)
```

結果を得るには反復処理が必要です。前述のように、複数の変数を使ってタプルを展開することができます。

```python
for column, value in pairs:
...
```

`zip` の一般的な使い方は、辞書を構築するためのキー/値のペアを作成することです。

```python
d = dict(zip(columns, values))
```
