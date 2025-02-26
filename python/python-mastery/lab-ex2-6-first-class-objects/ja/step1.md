# 一等公民データ

`portfolio.csv` ファイルでは、次のような列で構成されたデータを読み取りました。

```python
"AA",100,32.20
"IBM",50,91.10
...
```

以前のコードでは、すべての型変換をハードコーディングすることでこのデータを処理していました。たとえば：

```python
rows = csv.reader(f)
for row in rows:
    name   = row[0]
    shares = int(row[1])
    price  = float(row[2])
```

この種の変換は、いくつかのリスト操作を使ってもっと賢く行うこともできます。各列に対して行いたい変換を含むPythonのリストを作成しましょう。

```python
>>> coltypes = [str, int, float]
>>>
```

このリストを作成できる理由は、Pythonのすべてのものが「一等公民」だからです。つまり、関数のリストが欲しい場合でも問題ありません。

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

列の型と行をzip関数で結合して結果を見てみましょう。

```python
>>> r = list(zip(coltypes, row))
>>> r
[(<class'str'>, 'AA'), (<class 'int'>, '100'), (<class 'float'>,'32.20')]
>>>
```

これで型変換と値がペアになっていることがわかります。たとえば、`int` は値 `'100'` とペアになっています。次に、これを試してみましょう。

```python
>>> record = [func(val) for func, val in zip(coltypes, row)]
>>> record
['AA', 100, 32.2]
>>>
```

上記のコードで何が起こっているか必ず理解しておきましょう。ループ内では、`func` 変数は型変換関数の1つ（たとえば、`str`、`int` など）であり、`val` 変数は `'AA'`、`'100'` のような値の1つです。式 `func(val)` は値を変換しています（一種の型キャストのようなものです）。

さらに進めて、列ヘッダーを使って辞書を作成することもできます。たとえば：

```python
>>> dict(zip(headers, record))
{'name': 'AA','shares': 100, 'price': 32.2}
>>>
```

好きなように、辞書内包表記を使ってこれらのすべてのステップを一度に行うこともできます。

```python
>>> { name:func(val) for name, func, val in zip(headers, coltypes, row) }
{'name': 'AA','shares': 100, 'price': 32.2}
>>>
```
