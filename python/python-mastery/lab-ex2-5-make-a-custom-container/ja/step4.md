# カスタムコンテナクラスの作成

データ処理において、列指向アプローチはメモリを節約するのに優れています。しかし、既存のコードがデータを辞書のリスト形式で期待している場合、問題が発生することがあります。この問題を解決するために、カスタムコンテナクラスを作成します。このクラスは行指向のインターフェースを提供します。つまり、コードから見ると辞書のリストのように見え、動作します。ただし、内部的には列指向の形式でデータを格納し、メモリを節約するのに役立ちます。

1. まず、WebIDE エディタで `readrides.py` ファイルを開きます。このファイルに新しいクラスを追加します。このクラスがカスタムコンテナの基礎となります。

```python
# Add this to readrides.py
from collections.abc import Sequence

class RideData(Sequence):
    def __init__(self):
        # Each value is a list with all of the values (a column)
        self.routes = []
        self.dates = []
        self.daytypes = []
        self.numrides = []

    def __len__(self):
        # All lists assumed to have the same length
        return len(self.routes)

    def __getitem__(self, index):
        return {'route': self.routes[index],
                'date': self.dates[index],
                'daytype': self.daytypes[index],
                'rides': self.numrides[index]}

    def append(self, d):
        self.routes.append(d['route'])
        self.dates.append(d['date'])
        self.daytypes.append(d['daytype'])
        self.numrides.append(d['rides'])
```

このコードでは、`Sequence` を継承した `RideData` という名前のクラスを定義しています。`__init__` メソッドは、それぞれがデータの列を表す 4 つの空のリストを初期化します。`__len__` メソッドは、コンテナの長さを返します。これは `routes` リストの長さと同じです。`__getitem__` メソッドは、インデックスで特定のレコードにアクセスできるようにし、それを辞書として返します。`append` メソッドは、各列のリストに値を追加することで、新しいレコードをコンテナに追加します。

2. 次に、バスの乗車データをカスタムコンテナに読み込む関数が必要です。`readrides.py` ファイルに以下の関数を追加します。

```python
# Add this to readrides.py
def read_rides_as_dicts(filename):
    '''
    Read the bus ride data as a list of dicts, but use our custom container
    '''
    records = RideData()
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
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

この関数は、`RideData` クラスのインスタンスを作成し、CSV ファイルからのデータでそれを埋めます。ファイルから各行を読み取り、関連する情報を抽出し、各レコードに対して辞書を作成し、それを `RideData` コンテナに追加します。重要なのは、辞書のリストと同じインターフェースを維持しながら、内部的にはデータを列で格納することです。

3. Python シェルでカスタムコンテナをテストしましょう。これにより、期待通りに動作することを確認できます。

```python
import readrides

# Read the data using our custom container
rows = readrides.read_rides_as_dicts('ctabus.csv')

# Check the type of the returned object
type(rows)  # Should be readrides.RideData

# Check the length
len(rows)   # Should be 577563

# Access individual records
rows[0]     # Should return a dictionary for the first record
rows[1]     # Should return a dictionary for the second record
rows[2]     # Should return a dictionary for the third record
```

カスタムコンテナは `Sequence` インターフェースを正常に実装しています。つまり、リストのように振る舞います。`len()` 関数を使ってコンテナ内のレコード数を取得でき、インデックスを使って個々のレコードにアクセスできます。各レコードは辞書のように見えますが、内部的にはデータは列で格納されています。これは、辞書のリストを期待する既存のコードが、何の変更もせずにカスタムコンテナで動作し続けるので、非常に便利です。

4. 最後に、カスタムコンテナのメモリ使用量を測定しましょう。これにより、辞書のリストと比較してどれだけのメモリを節約できているかがわかります。

```python
import tracemalloc

tracemalloc.start()
rows = readrides.read_rides_as_dicts('ctabus.csv')
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage: {current/1024/1024:.2f} MB")
print(f"Peak memory usage: {peak/1024/1024:.2f} MB")
tracemalloc.stop()
```

このコードを実行すると、メモリ使用量が列指向アプローチと同程度であり、辞書のリストが使用するメモリよりもはるかに少ないことがわかるはずです。これは、メモリ効率の面でカスタムコンテナの利点を示しています。
