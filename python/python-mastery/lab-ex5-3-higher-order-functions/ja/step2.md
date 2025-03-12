# 高階関数の作成

Python では、高階関数とは、他の関数を引数として受け取ることができる関数です。これにより、より高い柔軟性とコードの再利用性が実現されます。では、`convert_csv()` という高階関数を作成しましょう。この関数は、CSV データを処理する共通の操作を担当し、CSV の各行をレコードに変換する方法をカスタマイズできるようにします。

WebIDE で `reader.py` ファイルを開きます。CSV データのイテラブル、変換関数、およびオプションとして列ヘッダーを受け取る関数を追加します。変換関数は、CSV の各行をレコードに変換するために使用されます。

以下は `convert_csv()` 関数のコードです。これを `reader.py` ファイルにコピーして貼り付けてください。

```python
def convert_csv(lines, conversion_func, *, headers=None):
    '''
    Convert lines of CSV data using the provided conversion function

    Args:
        lines: An iterable containing CSV data
        conversion_func: A function that takes headers and a row and returns a record
        headers: Column headers (optional). If None, the first row is used as headers

    Returns:
        A list of records as processed by conversion_func
    '''
    records = []
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)
    for row in rows:
        record = conversion_func(headers, row)
        records.append(record)
    return records
```

この関数が何をするかを分解してみましょう。まず、変換されたレコードを格納するために `records` という空のリストを初期化します。次に、`csv.reader()` 関数を使用して CSV データの行を読み取ります。ヘッダーが提供されていない場合、最初の行をヘッダーとして使用します。それ以降の各行について、`conversion_func` を適用して行をレコードに変換し、`records` リストに追加します。最後に、レコードのリストを返します。

では、`convert_csv()` 関数をテストするための簡単な変換関数が必要です。この関数は、ヘッダーと行を受け取り、ヘッダーをキーとして行を辞書に変換します。

以下は `make_dict()` 関数のコードです。この関数も `reader.py` ファイルに追加してください。

```python
def make_dict(headers, row):
    '''
    Convert a row to a dictionary using the provided headers
    '''
    return dict(zip(headers, row))
```

`make_dict()` 関数は、`zip()` 関数を使用して各ヘッダーを行内の対応する値とペアにし、それらのペアから辞書を作成します。

これらの関数をテストしましょう。ターミナルで以下のコマンドを実行して Python シェルを開きます。

```bash
cd ~/project
python3 -i reader.py
```

`python3` コマンドの `-i` オプションは、Python インタープリターを対話モードで起動し、`reader.py` ファイルをインポートするので、先ほど定義した関数を使用することができます。

Python シェルで、以下のコードを実行して関数をテストします。

```python
# Open the CSV file
lines = open('portfolio.csv')

# Convert to a list of dictionaries using our new function
result = convert_csv(lines, make_dict)

# Print the result
print(result)
```

このコードは `portfolio.csv` ファイルを開き、`convert_csv()` 関数と `make_dict()` 変換関数を使用して CSV データを辞書のリストに変換し、結果を出力します。

以下のような出力が表示されるはずです。

```
[{'name': 'AA', 'shares': '100', 'price': '32.20'}, {'name': 'IBM', 'shares': '50', 'price': '91.10'}, {'name': 'CAT', 'shares': '150', 'price': '83.44'}, {'name': 'MSFT', 'shares': '200', 'price': '51.23'}, {'name': 'GE', 'shares': '95', 'price': '40.37'}, {'name': 'MSFT', 'shares': '50', 'price': '65.10'}, {'name': 'IBM', 'shares': '100', 'price': '70.44'}]
```

この出力は、高階関数 `convert_csv()` が正しく動作していることを示しています。他の関数を引数として受け取る関数を成功裏に作成し、CSV データの変換方法を簡単に変更できるようになりました。

Python シェルを終了するには、`exit()` と入力するか、Ctrl+D を押します。
