# `enumerate()` と `zip()` 関数の使用

このステップでは、Python の反復処理に欠かせない 2 つの非常に便利な組み込み関数、`enumerate()` と `zip()` について探索します。これらの関数は、シーケンスを扱う際にコードを大幅に簡素化することができます。

## `enumerate()` を使ったカウント

シーケンスを反復処理する際に、各要素のインデックスや位置を追跡する必要があることがよくあります。そのような場合に `enumerate()` 関数が便利です。`enumerate()` 関数はシーケンスを入力として受け取り、そのシーケンス内の各要素に対して (インデックス，値) のペアを返します。

前のステップから Python インタープリターを使い続けている場合は、そのまま続けることができます。そうでない場合は、新しいセッションを開始します。新しく始める場合のデータのセットアップ方法は次のとおりです。

```python
# If you're starting a new session, reload the data first:
# import csv
# f = open('portfolio.csv')
# f_csv = csv.reader(f)
# headers = next(f_csv)
# rows = list(f_csv)

# Use enumerate to get row numbers
for rowno, row in enumerate(rows):
    print(rowno, row)
```

上記のコードを実行すると、`enumerate(rows)` 関数はインデックス (0 から始まる) と `rows` シーケンス内の対応する行のペアを生成します。`for` ループはこれらのペアを `rowno` と `row` という変数にアンパッキングし、それらを表示します。

出力：

```
0 ['AA', '100', '32.20']
1 ['IBM', '50', '91.10']
2 ['CAT', '150', '83.44']
3 ['MSFT', '200', '51.23']
4 ['GE', '95', '40.37']
5 ['MSFT', '50', '65.10']
6 ['IBM', '100', '70.44']
```

`enumerate()` とアンパッキングを組み合わせることで、コードをさらに読みやすくすることができます。アンパッキングを使うと、シーケンスの要素を個々の変数に直接割り当てることができます。

```python
for rowno, (name, shares, price) in enumerate(rows):
    print(rowno, name, shares, price)
```

このコードでは、`(name, shares, price)` の周りに追加の括弧を使って、行データを適切にアンパッキングしています。`enumerate(rows)` は依然としてインデックスと行を返しますが、今回は行を `name`、`shares`、`price` という変数にアンパッキングしています。

出力：

```
0 AA 100 32.20
1 IBM 50 91.10
2 CAT 150 83.44
3 MSFT 200 51.23
4 GE 95 40.37
5 MSFT 50 65.10
6 IBM 100 70.44
```

## `zip()` を使ったデータのペアリング

`zip()` 関数は Python のもう 1 つの強力なツールです。複数のシーケンスから対応する要素を組み合わせるために使われます。複数のシーケンスを `zip()` に渡すと、各タプルが入力シーケンスの同じ位置の要素を含むタプルを生成するイテレータが作成されます。

これまで扱ってきた `headers` と `row` のデータで `zip()` を使う方法を見てみましょう。

```python
# Recall the headers variable from earlier
print(headers)  # Should show ['name', 'shares', 'price']

# Get the first row
row = rows[0]
print(row)      # Should show ['AA', '100', '32.20']

# Use zip to pair column names with values
for col, val in zip(headers, row):
    print(col, val)
```

このコードでは、`zip(headers, row)` が `headers` シーケンスと `row` シーケンスを取り、それらの対応する要素をペアにします。`for` ループはこれらのペアを `col` (`headers` からの列名) と `val` (`row` からの値) にアンパッキングし、それらを表示します。

出力：

```
['name', 'shares', 'price']
['AA', '100', '32.20']
name AA
shares 100
price 32.20
```

`zip()` の非常に一般的な使い方の 1 つは、キーと値のペアから辞書を作成することです。Python では、辞書はキーと値のペアのコレクションです。

```python
# Create a dictionary from headers and row values
record = dict(zip(headers, row))
print(record)
```

ここでは、`zip(headers, row)` が列名と値のペアを作成し、`dict()` 関数がこれらのペアを辞書に変換します。

出力：

```
{'name': 'AA', 'shares': '100', 'price': '32.20'}
```

この考え方を拡張して、`rows` シーケンス内のすべての行を辞書に変換することができます。

```python
# Convert all rows to dictionaries
for row in rows:
    record = dict(zip(headers, row))
    print(record)
```

このループでは、`rows` 内の各行に対して、`zip(headers, row)` を使ってキーと値のペアを作成し、その後 `dict()` を使ってそれらのペアを辞書に変換します。この技術は、データ処理アプリケーション、特に最初の行にヘッダーが含まれる CSV ファイルを扱う際に非常に一般的です。

出力：

```
{'name': 'AA', 'shares': '100', 'price': '32.20'}
{'name': 'IBM', 'shares': '50', 'price': '91.10'}
{'name': 'CAT', 'shares': '150', 'price': '83.44'}
{'name': 'MSFT', 'shares': '200', 'price': '51.23'}
{'name': 'GE', 'shares': '95', 'price': '40.37'}
{'name': 'MSFT', 'shares': '50', 'price': '65.10'}
{'name': 'IBM', 'shares': '100', 'price': '70.44'}
```
