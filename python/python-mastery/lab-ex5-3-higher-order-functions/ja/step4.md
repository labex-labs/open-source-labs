# map() 関数の使用

Python では、高階関数とは、他の関数を引数として受け取ったり、関数を結果として返したりする関数です。Python の `map()` 関数は高階関数の良い例です。これは、リストやタプルなどのイテラブルの各要素に対して指定された関数を適用する強力なツールです。各要素に関数を適用した後、結果のイテレータを返します。この機能により、`map()` は CSV ファイルの行のようなデータ列の処理に最適です。

`map()` 関数の基本的な構文は以下の通りです。

```python
map(function, iterable, ...)
```

ここで、`function` は `iterable` の各要素に対して実行したい操作です。`iterable` はリストやタプルのような要素の列です。

簡単な例を見てみましょう。数値のリストがあり、そのリスト内の各数値を二乗したいとします。これを達成するために `map()` 関数を使用できます。以下はその方法です。

```python
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x * x, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]
```

この例では、まず `numbers` というリストを定義しています。次に、`map()` 関数を使用しています。`lambda` 関数 `lambda x: x * x` は、`numbers` リストの各要素に対して実行したい操作です。`map()` 関数はこの `lambda` 関数をリスト内の各数値に適用します。`map()` はイテレータを返すため、`list()` 関数を使用してリストに変換しています。最後に、元の数値を二乗した値を含む `squared` リストを出力します。

では、`map()` 関数を使って `convert_csv()` 関数をどのように修正できるか見てみましょう。以前は、CSV データの行を反復処理するために `for` ループを使用していました。今回は、その `for` ループを `map()` 関数に置き換えます。

```python
def convert_csv(lines, conversion_func, *, headers=None):
    '''
    Convert lines of CSV data using the provided conversion function
    '''
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)

    # Use map to apply conversion_func to each row
    records = list(map(lambda row: conversion_func(headers, row), rows))
    return records
```

この更新された `convert_csv()` 関数は、以前のバージョンとまったく同じことを行いますが、`for` ループの代わりに `map()` 関数を使用しています。`map()` 内の `lambda` 関数は、CSV データの各行を取得し、ヘッダーとともに `conversion_func` を適用します。

この更新された関数が正しく動作することを確認するためにテストしましょう。まず、ターミナルを開き、プロジェクトディレクトリに移動します。次に、`reader.py` ファイルを使って Python 対話型シェルを起動します。

```bash
cd ~/project
python3 -i reader.py
```

Python シェルに入ったら、以下のコードを実行して更新された `convert_csv()` 関数をテストします。

```python
# Test the updated convert_csv function
with open('portfolio.csv') as f:
    result = convert_csv(f, make_dict)
print(result[0])  # Should print the first dictionary

# Test that csv_as_dicts still works
with open('portfolio.csv') as f:
    portfolio = csv_as_dicts(f, [str, int, float])
print(portfolio[0])  # Should print the first dictionary with converted types
```

このコードを実行した後、以下のような出力が表示されるはずです。

```
{'name': 'AA', 'shares': '100', 'price': '32.20'}
{'name': 'AA', 'shares': 100, 'price': 32.2}
```

この出力は、`map()` 関数を使用した更新された `convert_csv()` 関数が正しく動作し、それに依存する関数も期待通りに動作し続けることを示しています。

`map()` 関数を使用することにはいくつかの利点があります。

1. `for` ループよりも簡潔に書けます。`for` ループのために複数行のコードを書く代わりに、`map()` を使って 1 行で同じ結果を得ることができます。
2. シーケンス内の各要素を変換する意図を明確に伝えます。`map()` を見ると、イテラブルの各要素に関数を適用していることがすぐにわかります。
3. イテレータを返すため、メモリ効率が良い場合があります。イテレータは値を逐次生成するため、一度にすべての結果をメモリに格納する必要がありません。この例では、`map()` が返すイテレータをリストに変換しましたが、場合によってはイテレータを直接使用してメモリを節約することができます。

Python シェルを終了するには、`exit()` と入力するか、Ctrl+D を押します。
