# 汎用的な CSV リーダーの作成

この最後のステップでは、汎用的な関数を作成します。この関数は CSV ファイルを読み込み、`from_row()` クラスメソッドを実装した任意のクラスのオブジェクトを作成することができます。これは、クラスメソッドを統一的なインターフェースとして使用する強力さを示しています。統一的なインターフェースとは、異なるクラスを同じように使用できることを意味し、これによりコードがより柔軟で管理しやすくなります。

## read_portfolio() 関数の修正

まず、`stock.py` ファイルの `read_portfolio()` 関数を更新します。新しい `from_row()` クラスメソッドを使用します。`stock.py` ファイルを開き、`read_portfolio()` 関数を次のように変更します。

```python
def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of Stock instances
    '''
    import csv
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)  # Skip header
        for row in rows:
            portfolio.append(Stock.from_row(row))
    return portfolio
```

この新しいバージョンの関数はよりシンプルです。型変換の責任を本当にそれが属する `Stock` クラスに委ねています。型変換とは、データをある型から別の型に変更することで、例えば文字列を整数に変換することです。こうすることで、コードがより整理され、理解しやすくなります。

## 汎用的な CSV リーダーの作成

次に、`reader.py` ファイルにより汎用的な関数を作成します。この関数は CSV データを読み込み、`from_row()` クラスメソッドを持つ任意のクラスのインスタンスを作成することができます。

`reader.py` ファイルを開き、次の関数を追加します。

```python
def read_csv_as_instances(filename, cls):
    '''
    Read a CSV file into a list of instances of the given class.

    Args:
        filename: Name of the CSV file
        cls: Class to instantiate (must have from_row class method)

    Returns:
        List of class instances
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)  # Skip header
        for row in rows:
            records.append(cls.from_row(row))
    return records
```

この関数は2つの入力を受け取ります。ファイル名とクラスです。そして、CSV ファイルのデータから作成されたそのクラスのインスタンスのリストを返します。これは非常に便利です。なぜなら、`from_row()` メソッドを持つ限り、異なるクラスで使用することができるからです。

## 汎用的な CSV リーダーのテスト

汎用的なリーダーがどのように動作するかを確認するために、テストファイルを作成しましょう。次の内容で `test_csv_reader.py` という名前のファイルを作成します。

```python
# test_csv_reader.py
from reader import read_csv_as_instances
from stock import Stock
from decimal_stock import DStock

# Read portfolio as Stock instances
portfolio = read_csv_as_instances('portfolio.csv', Stock)
print(f"Portfolio contains {len(portfolio)} stocks")
print(f"First stock: {portfolio[0].name}, {portfolio[0].shares} shares at ${portfolio[0].price}")

# Read portfolio as DStock instances (with Decimal prices)
decimal_portfolio = read_csv_as_instances('portfolio.csv', DStock)
print(f"\nDecimal portfolio contains {len(decimal_portfolio)} stocks")
print(f"First stock: {decimal_portfolio[0].name}, {decimal_portfolio[0].shares} shares at ${decimal_portfolio[0].price}")

# Define a new class for reading the bus data
class BusRide:
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

    @classmethod
    def from_row(cls, row):
        return cls(row[0], row[1], row[2], int(row[3]))

# Read some bus data (just the first 5 records for brevity)
print("\nReading bus data...")
import csv
with open('ctabus.csv') as f:
    rows = csv.reader(f)
    headers = next(rows)  # Skip header
    bus_rides = []
    for i, row in enumerate(rows):
        if i >= 5:  # Only read 5 records for the example
            break
        bus_rides.append(BusRide.from_row(row))

# Display the bus data
for ride in bus_rides:
    print(f"Route: {ride.route}, Date: {ride.date}, Type: {ride.daytype}, Rides: {ride.rides}")
```

このファイルを実行して結果を確認します。ターミナルを開き、次のコマンドを使用します。

```bash
cd ~/project
python test_csv_reader.py
```

`Stock` と `DStock` の両方のインスタンスとして読み込まれたポートフォリオデータ、および `BusRide` インスタンスとして読み込まれたバス路線データが表示されるはずです。これは、汎用的なリーダーが異なるクラスで動作することを証明しています。

## このアプローチの主な利点

このアプローチはいくつかの強力な概念を示しています。

1. **関心事の分離**：データの読み込みとオブジェクトの作成が分離されています。これは、CSV ファイルを読み込むコードがオブジェクトを作成するコードと混在しないことを意味します。コードが理解しやすく、保守しやすくなります。
2. **ポリモーフィズム**：同じコードが同じインターフェースに従う異なるクラスで動作することができます。この場合、クラスが `from_row()` メソッドを持っている限り、汎用的なリーダーはそれを使用することができます。
3. **柔軟性**：異なるクラスを使用することで、データの変換方法を簡単に変更することができます。例えば、`Stock` または `DStock` を使用して、ポートフォリオデータを異なる方法で処理することができます。
4. **拡張性**：リーダーのコードを変更することなく、リーダーと互換性のある新しいクラスを追加することができます。これにより、コードが将来に対応しやすくなります。

これは Python で一般的なパターンであり、コードをよりモジュール化、再利用可能、保守可能にします。

## クラスメソッドに関する最後の注意

クラスメソッドは Python で代替コンストラクタとしてよく使用されます。通常、その名前に "from" という単語が含まれていることで区別できます。例えば：

```python
# Some examples from Python's built-in types
dict.fromkeys(['a', 'b', 'c'], 0)  # Create a dict with default values
datetime.datetime.fromtimestamp(1627776000)  # Create datetime from timestamp
int.from_bytes(b'\x00\x01', byteorder='big')  # Create int from bytes
```

この規則に従うことで、コードがより読みやすくなり、Python の組み込みライブラリとの一貫性が保たれます。これにより、他の開発者がコードをより簡単に理解することができます。
