# 列指向のデータストレージ

これまで、CSV データを行辞書のリストとして格納してきました。これは、CSV ファイルの各行が辞書として表され、キーが列ヘッダーで値がその行の対応するデータであることを意味します。しかし、大規模なデータセットを扱う場合、この方法は非効率的です。列指向の形式でデータを格納する方が良い選択肢となります。列指向のアプローチでは、各列のデータが別々のリストに格納されます。これにより、同じデータ型がグループ化されるため、メモリ使用量を大幅に削減でき、列ごとのデータ集計などの特定の操作のパフォーマンスも向上させることができます。

## 列指向のデータリーダーの作成

ここでは、列指向の形式で CSV データを読み取るのに役立つ新しいファイルを作成します。プロジェクトディレクトリに `colreader.py` という名前の新しいファイルを作成し、以下のコードを記述します。

```python
import csv

class DataCollection:
    def __init__(self, headers, columns):
        """
        Initialize a column-oriented data collection.

        Parameters:
        headers (list): Column header names
        columns (dict): Dictionary mapping header names to column data lists
        """
        self.headers = headers
        self.columns = columns
        self._length = len(columns[headers[0]]) if headers else 0

    def __len__(self):
        """Return the number of rows in the collection."""
        return self._length

    def __getitem__(self, index):
        """
        Get a row by index, presented as a dictionary.

        Parameters:
        index (int): Row index

        Returns:
        dict: Dictionary representing the row at the given index
        """
        if isinstance(index, int):
            if index < 0 or index >= self._length:
                raise IndexError("Index out of range")

            return {header: self.columns[header][index] for header in self.headers}
        else:
            raise TypeError("Index must be an integer")

def read_csv_as_columns(filename, types):
    """
    Read a CSV file into a column-oriented data structure, converting each field
    according to the types provided.

    Parameters:
    filename (str): Name of the CSV file to read
    types (list): List of type conversion functions for each column

    Returns:
    DataCollection: Column-oriented data collection representing the CSV data
    """
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)  # Get the column headers

        # Initialize columns
        columns = {header: [] for header in headers}

        # Read data into columns
        for row in rows:
            # Convert values according to the specified types
            converted_values = [func(val) for func, val in zip(types, row)]

            # Add each value to its corresponding column
            for header, value in zip(headers, converted_values):
                columns[header].append(value)

    return DataCollection(headers, columns)
```

このコードは 2 つの重要なことを行います。

1. `DataCollection` クラスを定義します。このクラスはデータを列で格納しますが、データを行辞書のリストのようにアクセスできるようにします。これは、データを扱う際に馴染みのある方法を提供するために便利です。
2. `read_csv_as_columns` 関数を定義します。この関数は、CSV ファイルからデータを読み取り、列指向の構造に格納します。また、提供された型に従って CSV ファイルの各フィールドを変換します。

## 列指向のリーダーのテスト

CTA バスデータを使用して、列指向のリーダーをテストしましょう。まず、Python インタープリタを開きます。ターミナルで以下のコマンドを実行することで、これを行うことができます。

```bash
python3
```

Python インタープリタが開いたら、以下のコードを実行します。

```python
import colreader
import tracemalloc
from sys import intern

# Start memory tracking
tracemalloc.start()

# Read data into column-oriented structure with string interning
data = colreader.read_csv_as_columns('ctabus.csv', [intern, intern, intern, int])

# Check that we can access the data like a list of dictionaries
print(f"Number of rows: {len(data)}")
print("First 3 rows:")
for i in range(3):
    print(data[i])

# Check memory usage
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage: {current / 1024 / 1024:.2f} MB")
print(f"Peak memory usage: {peak / 1024 / 1024:.2f} MB")
```

出力は以下のようになるはずです。

```
Number of rows: 577563
First 3 rows:
{'route': '3', 'date': '01/01/2001', 'daytype': 'U', 'rides': 7354}
{'route': '4', 'date': '01/01/2001', 'daytype': 'U', 'rides': 9288}
{'route': '6', 'date': '01/01/2001', 'daytype': 'U', 'rides': 6048}
Current memory usage: 38.67 MB
Peak memory usage: 103.42 MB
```

では、これを以前の行指向のアプローチと比較してみましょう。同じ Python インタープリタで以下のコードを実行します。

```python
import reader
import tracemalloc
from sys import intern

# Reset memory tracking
tracemalloc.reset_peak()

# Read data into row-oriented structure with string interning
rows = reader.read_csv_as_dicts('ctabus.csv', [intern, intern, intern, int])

# Check memory usage
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage (row-oriented): {current / 1024 / 1024:.2f} MB")
print(f"Peak memory usage (row-oriented): {peak / 1024 / 1024:.2f} MB")
```

出力は以下のようになるはずです。

```
Current memory usage (row-oriented): 170.23 MB
Peak memory usage (row-oriented): 190.05 MB
```

ご覧の通り、列指向のアプローチは大幅に少ないメモリを使用します！

また、以前と同じようにデータを分析できることもテストしてみましょう。以下のコードを実行します。

```python
# Find all unique routes in the column-oriented data
routes = {row['route'] for row in data}
print(f"Number of unique routes: {len(routes)}")

# Count rides per route (first 5)
from collections import defaultdict
route_rides = defaultdict(int)
for row in data:
    route_rides[row['route']] += row['rides']

# Show the top 5 routes by total rides
top_routes = sorted(route_rides.items(), key=lambda x: x[1], reverse=True)[:5]
print("Top 5 routes by total rides:")
for route, rides in top_routes:
    print(f"Route {route}: {rides:,} rides")
```

出力は以下のようになるはずです。

```
Number of unique routes: 181
Top 5 routes by total rides:
Route 9: 158,545,826 rides
Route 49: 129,872,910 rides
Route 77: 120,086,065 rides
Route 79: 109,348,708 rides
Route 4: 91,405,538 rides
```

最後に、以下のコマンドを実行して Python インタープリタを終了します。

```python
exit()
```

列指向のアプローチはメモリを節約するだけでなく、以前と同じ分析を行うこともできることがわかります。これは、異なるデータストレージ戦略がパフォーマンスに大きな影響を与える一方で、データを扱うための同じインターフェースを提供することを示しています。
