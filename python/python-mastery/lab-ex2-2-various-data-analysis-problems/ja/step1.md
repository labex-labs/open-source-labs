# 辞書とCSVデータの扱い

まずは、株式保有に関する簡単なデータセットを調べてみましょう。このステップでは、CSVファイルからデータを読み取り、辞書を使って構造化された形式で保存する方法を学びます。

CSV（Comma-Separated Values、カンマ区切り値）ファイルは、表形式のデータを保存する一般的な方法で、各行が1つのレコードを表し、値はカンマで区切られています。Pythonの辞書は、キーと値のペアを格納できる強力なデータ構造です。辞書を使うことで、CSVファイルからのデータをより意味のある形で整理することができます。

まず、WebIDEで新しいPythonファイルを作成します。手順は以下の通りです。

1. WebIDEの「New File」ボタンをクリックします。
2. ファイル名を`readport.py`とします。
3. 以下のコードをファイルにコピーして貼り付けます。

```python
# readport.py

import csv

# A function that reads a file into a list of dictionaries
def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)   # Skip the header row
        for row in rows:
            record = {
                'name': row[0],
                'shares': int(row[1]),
                'price': float(row[2])
            }
            portfolio.append(record)
    return portfolio
```

このコードは、`read_portfolio`という関数を定義しており、いくつかの重要なタスクを実行します。

1. `filename`パラメータで指定されたCSVファイルを開きます。`open`関数を使ってファイルにアクセスし、`with`文を使ってファイルの読み取りが終わった後に適切に閉じることを保証します。
2. ヘッダ行をスキップします。ヘッダ行には通常、CSVファイルの列名が含まれています。`next(rows)`を使ってイテレータを次の行に移動させ、ヘッダ行をスキップします。
3. 各データ行に対して、辞書を作成します。辞書のキーは'name'、'shares'、'price'です。これらのキーを使うことで、データにより直感的にアクセスすることができます。
4. 株式数を整数に、価格を浮動小数点数に変換します。CSVファイルから読み取ったデータは最初は文字列形式であるため、計算には数値が必要です。
5. 各辞書を`portfolio`というリストに追加します。このリストには、CSVファイルのすべてのレコードが含まれます。
6. 最後に、辞書の完全なリストを返します。

次に、交通データ用のファイルを作成しましょう。`readrides.py`という名前の新しいファイルを作成し、以下の内容を記述します。

```python
# readrides.py

import csv

def read_rides_as_dicts(filename):
    """
    Read the CTA bus data as a list of dictionaries
    """
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)   # Skip header
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = {
                'route': route,
                'date': date,
                'daytype': daytype,
                'rides': rides
            }
            records.append(record)
    return records
```

この`read_rides_as_dicts`関数は、`read_portfolio`関数と同様の動作をします。CTAバスデータに関連するCSVファイルを読み取り、ヘッダ行をスキップし、各データ行に対して辞書を作成し、これらの辞書をリストに格納します。

では、WebIDEでターミナルを開き、`read_portfolio`関数をテストしましょう。

1. 「Terminal」メニューをクリックし、「New Terminal」を選択します。
2. `python3`と入力してPythonインタープリタを起動します。
3. 以下のコマンドを実行します。

```python
>>> from readport import read_portfolio
>>> portfolio = read_portfolio('/home/labex/project/portfolio.csv')
>>> from pprint import pprint
>>> pprint(portfolio)
[{'name': 'AA', 'price': 32.2, 'shares': 100},
 {'name': 'IBM', 'price': 91.1, 'shares': 50},
 {'name': 'CAT', 'price': 83.44, 'shares': 150},
 {'name': 'MSFT', 'price': 51.23, 'shares': 200},
 {'name': 'GE', 'price': 40.37, 'shares': 95},
 {'name': 'MSFT', 'price': 65.1, 'shares': 50},
 {'name': 'IBM', 'price': 70.44, 'shares': 100}]
```

ここでは、`pprint`関数（整形出力）を使ってデータをより読みやすい形式で表示しています。リスト内の各アイテムは、1つの株式保有を表す辞書です。辞書には以下のキーがあります。

- 株式シンボル (`name`)：株式を識別するために使用される略称です。
- 保有株式数 (`shares`)：保有している株式の数を示します。
- 1株あたりの購入価格 (`price`)：各株を購入した価格です。

'MSFT'や'IBM'などの一部の株式が複数回出現していることに注意してください。これらは、同じ株式の異なる購入を表しており、異なる時期に異なる価格で購入された可能性があります。
