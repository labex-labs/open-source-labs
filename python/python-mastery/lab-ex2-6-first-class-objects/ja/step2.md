# CSV処理用のユーティリティ関数の作成

Pythonの第一級オブジェクトがデータ変換にどのように役立つかを理解したので、再利用可能なユーティリティ関数を作成します。この関数はCSVデータを読み取り、辞書のリストに変換します。これは非常に有用な操作です。なぜなら、CSVファイルは表形式のデータを格納するために一般的に使用されており、これを辞書のリストに変換することで、Pythonでデータを扱いやすくなるからです。

## CSVリーダーユーティリティの作成

まず、WebIDEを開きます。開いたら、プロジェクトディレクトリに移動し、`reader.py` という名前の新しいファイルを作成します。このファイルでは、CSVデータを読み取り、型変換を適用する関数を定義します。型変換は重要です。なぜなら、CSVファイル内のデータは通常文字列として読み取られますが、さらなる処理のために整数や浮動小数点数などの異なるデータ型が必要になることがあるからです。

`reader.py` に以下のコードを追加します。

```python
import csv

def read_csv_as_dicts(filename, types):
    """
    Read a CSV file into a list of dictionaries, converting each field according
    to the types provided.

    Parameters:
    filename (str): Name of the CSV file to read
    types (list): List of type conversion functions for each column

    Returns:
    list: List of dictionaries representing the CSV data
    """
    records = []
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)  # Get the column headers

        for row in rows:
            # Apply type conversions to each value in the row
            converted_row = [func(val) for func, val in zip(types, row)]

            # Create a dictionary mapping headers to converted values
            record = dict(zip(headers, converted_row))
            records.append(record)

    return records
```

この関数はまず、指定されたCSVファイルを開きます。次に、CSVファイルのヘッダー（列名）を読み取ります。その後、ファイル内の各行を処理します。行内の各値に対して、`types` リストから対応する型変換関数を適用します。最後に、キーが列ヘッダーで値が変換されたデータである辞書を作成し、この辞書を `records` リストに追加します。すべての行が処理されると、`records` リストを返します。

## ユーティリティ関数のテスト

ユーティリティ関数をテストしましょう。まず、ターミナルを開き、以下を入力してPythonインタープリタを起動します。

```bash
python3
```

Pythonインタープリタに入ったら、関数を使用してポートフォリオデータを読み取ることができます。ポートフォリオデータは、株式の名前、株式数、価格などの株式に関する情報を含むCSVファイルです。

```python
import reader
portfolio = reader.read_csv_as_dicts('portfolio.csv', [str, int, float])
for record in portfolio[:3]:  # Show the first 3 records
    print(record)
```

このコードを実行すると、以下のような出力が表示されるはずです。

```
{'name': 'AA', 'shares': 100, 'price': 32.2}
{'name': 'IBM', 'shares': 50, 'price': 91.1}
{'name': 'CAT', 'shares': 150, 'price': 83.44}
```

この出力は、ポートフォリオデータの最初の3つのレコードを示しており、データ型が正しく変換されています。

CTAバスデータでも関数を試してみましょう。CTAバスデータは、バス路線、日付、曜日タイプ、乗車人数に関する情報を含む別のCSVファイルです。

```python
rows = reader.read_csv_as_dicts('ctabus.csv', [str, str, str, int])
print(f"Total rows: {len(rows)}")
print("First row:", rows[0])
```

出力は以下のようになるはずです。

```
Total rows: 577563
First row: {'route': '3', 'date': '01/01/2001', 'daytype': 'U', 'rides': 7354}
```

これは、関数が異なるCSVファイルを処理し、適切な型変換を適用できることを示しています。

Pythonインタープリタを終了するには、以下を入力します。

```python
exit()
```

これで、任意のCSVファイルを読み取り、適切な型変換を適用できる再利用可能なユーティリティ関数を作成しました。これは、Pythonの第一級オブジェクトの強力さと、柔軟で再利用可能なコードを作成するための使い方を示しています。
