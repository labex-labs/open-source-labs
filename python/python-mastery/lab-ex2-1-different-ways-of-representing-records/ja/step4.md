# 異なるデータ構造の比較

Python では、データ構造を使用して関連するデータを整理し、保存します。データ構造は、構造化された方法でさまざまな種類の情報を保持するコンテナのようなものです。このステップでは、異なるデータ構造を比較し、それぞれがどれだけのメモリを使用するかを見ていきます。

`/home/labex/project` ディレクトリに `compare_structures.py` という名前の新しいファイルを作成しましょう。このファイルには、CSV ファイルからデータを読み込み、異なるデータ構造に保存するコードが含まれます。

```python
# compare_structures.py
import csv
import tracemalloc
from collections import namedtuple

# 乗車データ用の名前付きタプルを定義する
RideRecord = namedtuple('RideRecord', ['route', 'date', 'daytype', 'rides'])

# 名前付きタプルは、フィールドに名前でアクセスできる軽量クラスです。
# タプルのようなものですが、名前付き属性を持っています。

# メモリ最適化のために __slots__ を持つクラスを定義する
class SlottedRideRecord:
    __slots__ = ['route', 'date', 'daytype', 'rides']

    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

# __slots__ を持つクラスは、メモリが最適化されたクラスです。
# インスタンス辞書を使用しないため、メモリを節約します。

# 乗車データ用の通常のクラスを定義する
class RegularRideRecord:
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

# 通常のクラスは、データを表現するオブジェクト指向の方法です。
# 名前付き属性を持ち、メソッドを持つことができます。

# データをタプルとして読み込む関数
def read_as_tuples(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        next(rows)  # ヘッダーをスキップする
        for row in rows:
            record = (row[0], row[1], row[2], int(row[3]))
            records.append(record)
    return records

# この関数は、CSV ファイルからデータを読み込み、タプルとして保存します。
# タプルは不変のシーケンスであり、要素には数値インデックスでアクセスします。

# データを辞書として読み込む関数
def read_as_dicts(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)  # ヘッダーを取得する
        for row in rows:
            record = {
                'route': row[0],
                'date': row[1],
                'daytype': row[2],
                'rides': int(row[3])
            }
            records.append(record)
    return records

# この関数は、CSV ファイルからデータを読み込み、辞書として保存します。
# 辞書はキーと値のペアを使用するため、要素に名前でアクセスできます。

# データを名前付きタプルとして読み込む関数
def read_as_named_tuples(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        next(rows)  # ヘッダーをスキップする
        for row in rows:
            record = RideRecord(row[0], row[1], row[2], int(row[3]))
            records.append(record)
    return records

# この関数は、CSV ファイルからデータを読み込み、名前付きタプルとして保存します。
# 名前付きタプルは、タプルの効率性と名前によるアクセスの読みやすさを兼ね備えています。

# データを通常のクラスのインスタンスとして読み込む関数
def read_as_regular_classes(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        next(rows)  # ヘッダーをスキップする
        for row in rows:
            record = RegularRideRecord(row[0], row[1], row[2], int(row[3]))
            records.append(record)
    return records

# この関数は、CSV ファイルからデータを読み込み、通常のクラスのインスタンスとして保存します。
# 通常のクラスを使用すると、データにメソッドを追加できます。

# データを __slots__ を持つクラスのインスタンスとして読み込む関数
def read_as_slotted_classes(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        next(rows)  # ヘッダーをスキップする
        for row in rows:
            record = SlottedRideRecord(row[0], row[1], row[2], int(row[3]))
            records.append(record)
    return records

# この関数は、CSV ファイルからデータを読み込み、__slots__ を持つクラスのインスタンスとして保存します。
# __slots__ を持つクラスはメモリが最適化されており、名前によるアクセスも提供します。

# メモリ使用量を測定する関数
def measure_memory(func, filename):
    tracemalloc.start()

    records = func(filename)

    current, peak = tracemalloc.get_traced_memory()

    # 各データ構造の使用方法を示す
    first_record = records[0]
    if func.__name__ == 'read_as_tuples':
        route, date, daytype, rides = first_record
    elif func.__name__ == 'read_as_dicts':
        route = first_record['route']
        date = first_record['date']
        daytype = first_record['daytype']
        rides = first_record['rides']
    else:  # 名前付きタプルとクラス
        route = first_record.route
        date = first_record.date
        daytype = first_record.daytype
        rides = first_record.rides

    print(f"Structure type: {func.__name__}")
    print(f"Record count: {len(records)}")
    print(f"Example access: Route={route}, Date={date}, Rides={rides}")
    print(f"Current memory: {current/1024/1024:.2f} MB")
    print(f"Peak memory: {peak/1024/1024:.2f} MB")
    print("-" * 50)

    tracemalloc.stop()

    return current

if __name__ == "__main__":
    filename = '/home/labex/project/ctabus.csv'

    # すべてのメモリテストを実行する
    print("Memory usage comparison for different data structures:\n")

    results = []
    for reader_func in [
        read_as_tuples,
        read_as_dicts,
        read_as_named_tuples,
        read_as_regular_classes,
        read_as_slotted_classes
    ]:
        memory = measure_memory(reader_func, filename)
        results.append((reader_func.__name__, memory))

    # メモリ使用量でソートする（少ない順）
    results.sort(key=lambda x: x[1])

    print("\nRanking by memory efficiency (most efficient first):")
    for i, (name, memory) in enumerate(results, 1):
        print(f"{i}. {name}: {memory/1024/1024:.2f} MB")
```

比較結果を確認するには、スクリプトを実行します。

```bash
python3 /home/labex/project/compare_structures.py
```

出力には、各データ構造のメモリ使用量と、メモリ効率の高い順から低い順のランキングが表示されます。

## 異なるデータ構造の理解

1. **タプル**:
   - タプルは軽量で不変のシーケンスです。つまり、タプルを作成した後は、その要素を変更することができません。
   - タプルの要素には、`record[0]`、`record[1]` などの数値インデックスでアクセスします。
   - 構造がシンプルなため、メモリ効率が非常に高いです。
   - ただし、各要素のインデックスを覚える必要があるため、読みやすさが劣ることがあります。

2. **辞書**:
   - 辞書はキーと値のペアを使用するため、要素に名前でアクセスできます。
   - 例えば、`record['route']`、`record['date']` などを使用できるため、読みやすさが高いです。
   - キーと値のペアを保存するためにハッシュテーブルのオーバーヘッドがあるため、メモリ使用量が多くなります。
   - フィールドの追加や削除が容易なため、柔軟性が高いです。

3. **名前付きタプル**:
   - 名前付きタプルは、タプルの効率性と要素に名前でアクセスする機能を兼ね備えています。
   - `record.route`、`record.date` などのドット表記を使用して要素にアクセスできます。
   - 通常のタプルと同様に不変です。
   - 辞書よりもメモリ効率が高いです。

4. **通常のクラス**:
   - 通常のクラスはオブジェクト指向のアプローチに従い、名前付き属性を持っています。
   - `record.route`、`record.date` などのドット表記を使用して属性にアクセスできます。
   - 通常のクラスには、振る舞いを定義するメソッドを追加できます。
   - 各インスタンスに属性を保存するためのインスタンス辞書があるため、メモリ使用量が多くなります。

5. \***\*slots** を持つクラス\*\*:
   - `__slots__` を持つクラスはメモリが最適化されたクラスです。インスタンス辞書を使用しないため、メモリを節約します。
   - `record.route`、`record.date` などの名前による属性へのアクセスを提供します。
   - オブジェクトを作成した後は、新しい属性の追加が制限されます。
   - 通常のクラスよりもメモリ効率が高いです。

## 各アプローチの使用時期

- **タプル**: メモリが重要な要素であり、データに単純なインデックスアクセスのみが必要な場合に使用します。
- **辞書**: データのフィールドが変化する可能性があるなど、柔軟性が必要な場合に使用します。
- **名前付きタプル**: 読みやすさとメモリ効率の両方が必要な場合に使用します。
- **通常のクラス**: データに振る舞い（メソッド）を追加する必要がある場合に使用します。
- \***\*slots** を持つクラス\*\*: 振る舞いと最大限のメモリ効率が必要な場合に使用します。

必要に応じて適切なデータ構造を選択することで、特に大規模なデータセットを扱う場合に、Python プログラムのパフォーマンスとメモリ使用量を大幅に改善することができます。
