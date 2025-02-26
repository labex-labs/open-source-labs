# 演習2.24: 一等公民データ

`portfolio.csv` ファイルには、次のような列で整理されたデータが含まれています。

```csv
name,shares,price
"AA",100,32.20
"IBM",50,91.10
...
```

以前のコードでは、`csv` モジュールを使ってファイルを読み取りましたが、手動で型変換を行う必要がありました。たとえば:

```python
for row in rows:
    name   = row[0]
    shares = int(row[1])
    price  = float(row[2])
```

この種の変換は、いくつかのリスト基本操作を使って、もっと賢く行うこともできます。

各列を適切な型に変換するために使用する変換関数の名前を含むPythonリストを作成してください。

```python
>>> types = [str, int, float]
>>>
```

Pythonではすべてが _一等公民_ であるため、このようなリストを作成できるのです。つまり、関数のリストが欲しい場合でも問題ありません。作成したリストの要素は、値 `x` を指定された型に変換する関数です (たとえば、`str(x)`、`int(x)`、`float(x)` など)。

次に、上記のファイルから1行のデータを読み取ります。

```python
>>> import csv
>>> f = open('portfolio.csv')
>>> rows = csv.reader(f)
>>> headers = next(rows)
>>> row = next(rows)
>>> row
['AA', '100', '32.20']
>>>
```

前述の通り、この行だけでは計算を行うことができません。なぜなら型が正しくないからです。たとえば:

```python
>>> row[1] * row[2]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type'str'
>>>
```

しかし、データを `types` に指定した型とペアにすることができるかもしれません。たとえば:

```python
>>> types[1]
<type 'int'>
>>> row[1]
'100'
>>>
```

値の1つを変換してみましょう。

```python
>>> types[1](row[1])     # Same as int(row[1])
100
>>>
```

別の値を変換してみましょう。

```python
>>> types[2](row[2])     # Same as float(row[2])
32.2
>>>
```

変換後の値を使って計算を試してみましょう。

```python
>>> types[1](row[1])*types[2](row[2])
3220.0000000000005
>>>
```

列の型とフィールドをzipして結果を見てみましょう。

```python
>>> r = list(zip(types, row))
>>> r
[(<type'str'>, 'AA'), (<type 'int'>, '100'), (<type 'float'>,'32.20')]
>>>
```

これで型変換と値がペアになっていることがわかります。たとえば、`int` は値 `'100'` とペアになっています。

zipされたリストは、すべての値に対して1つずつ型変換を行いたい場合に便利です。試してみましょう。

```python
>>> converted = []
>>> for func, val in zip(types, row):
          converted.append(func(val))
...
>>> converted
['AA', 100, 32.2]
>>> converted[1] * converted[2]
3220.0000000000005
>>>
```

上記のコードで何が起こっているか必ず理解してください。ループ内では、`func` 変数は型変換関数の1つ (たとえば、`str`、`int` など) であり、`val` 変数は `'AA'`、`'100'` のような値の1つです。式 `func(val)` は値を変換しています (一種の型キャストのようなものです)。

上記のコードは、単一のリスト内包表記に圧縮することができます。

```python
>>> converted = [func(val) for func, val in zip(types, row)]
>>> converted
['AA', 100, 32.2]
>>>
```
