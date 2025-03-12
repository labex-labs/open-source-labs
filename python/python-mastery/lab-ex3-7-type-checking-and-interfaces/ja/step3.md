# アルゴリズムテンプレートクラスの作成

このステップでは、抽象基底クラスを使用してテンプレートメソッドパターンを実装します。目的は、CSV 解析機能におけるコードの重複を削減することです。コードの重複は、コードの保守と更新を困難にする可能性があります。テンプレートメソッドパターンを使用することで、CSV 解析コードの共通構造を作成し、サブクラスに具体的な詳細を処理させることができます。

## テンプレートメソッドパターンの理解

テンプレートメソッドパターンは、振る舞いに関するデザインパターンです。アルゴリズムの青写真のようなものです。メソッド内で、アルゴリズムの全体的な構造または「骨格」を定義します。ただし、すべてのステップを完全に実装するわけではありません。代わりに、一部のステップをサブクラスに委譲します。これは、サブクラスがアルゴリズムの特定の部分を再定義できる一方で、その全体構造を変更することなく実現できることを意味します。

私たちのケースでは、`reader.py` ファイルを見ると、`read_csv_as_dicts()` 関数と `read_csv_as_instances()` 関数には多くの類似したコードがあることに気づくでしょう。これらの主な違いは、CSV ファイルの行からレコードを作成する方法です。テンプレートメソッドパターンを使用することで、同じコードを複数回書くことを避けることができます。

## CSVParser 基底クラスの追加

まず、CSV 解析用の抽象基底クラスを追加しましょう。`reader.py` ファイルを開きます。インポート文の直後に、`CSVParser` 抽象基底クラスをファイルの先頭に追加します。

```python
# reader.py
import csv
from abc import ABC, abstractmethod

class CSVParser(ABC):
    def parse(self, filename):
        records = []
        with open(filename) as f:
            rows = csv.reader(f)
            headers = next(rows)
            for row in rows:
                record = self.make_record(headers, row)
                records.append(record)
        return records

    @abstractmethod
    def make_record(self, headers, row):
        pass
```

この `CSVParser` クラスは、CSV 解析のテンプレートとして機能します。`parse` メソッドには、CSV ファイルを読み取るための共通のステップが含まれています。たとえば、ファイルを開く、ヘッダーを取得する、行を反復処理するなどです。行からレコードを作成する具体的なロジックは、`make_record()` メソッドに抽象化されています。これは抽象メソッドであるため、`CSVParser` を継承するすべてのクラスはこのメソッドを実装しなければなりません。

## 具体的なパーサークラスの実装

これで基底クラスができたので、具体的なパーサークラスを作成する必要があります。これらのクラスは、具体的なレコード作成ロジックを実装します。

```python
class DictCSVParser(CSVParser):
    def __init__(self, types):
        self.types = types

    def make_record(self, headers, row):
        return { name: func(val) for name, func, val in zip(headers, self.types, row) }

class InstanceCSVParser(CSVParser):
    def __init__(self, cls):
        self.cls = cls

    def make_record(self, headers, row):
        return self.cls.from_row(row)
```

`DictCSVParser` クラスは、レコードを辞書として作成するために使用されます。コンストラクタで型のリストを受け取ります。`make_record` メソッドは、これらの型を使用して行内の値を変換し、辞書を作成します。

`InstanceCSVParser` クラスは、レコードをクラスのインスタンスとして作成するために使用されます。コンストラクタでクラスを受け取ります。`make_record` メソッドは、そのクラスの `from_row` メソッドを呼び出して、行からインスタンスを作成します。

## 元の関数のリファクタリング

では、元の `read_csv_as_dicts()` 関数と `read_csv_as_instances()` 関数をリファクタリングして、これらの新しいクラスを使用するようにしましょう。

```python
def read_csv_as_dicts(filename, types):
    '''
    Read a CSV file into a list of dictionaries with appropriate type conversion.
    '''
    parser = DictCSVParser(types)
    return parser.parse(filename)

def read_csv_as_instances(filename, cls):
    '''
    Read a CSV file into a list of instances of a class.
    '''
    parser = InstanceCSVParser(cls)
    return parser.parse(filename)
```

これらのリファクタリングされた関数は、元の関数と同じインターフェースを持っています。ただし、内部的には、先ほど作成した新しいパーサークラスを使用しています。このようにして、共通の CSV 解析ロジックと具体的なレコード作成ロジックを分離しました。

## 実装のテスト

リファクタリングしたコードが正しく動作するか確認しましょう。`test_reader.py` という名前のファイルを作成し、以下のコードを追加します。

```python
import reader
import stock

# Test the refactored read_csv_as_instances function
portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
print("First stock:", portfolio[0])

# Test the refactored read_csv_as_dicts function
portfolio_dicts = reader.read_csv_as_dicts('portfolio.csv', [str, int, float])
print("First stock as dict:", portfolio_dicts[0])

# Test direct use of a parser
parser = reader.DictCSVParser([str, int, float])
portfolio_dicts2 = parser.parse('portfolio.csv')
print("First stock from direct parser:", portfolio_dicts2[0])
```

テストを実行するには、ターミナルを開き、次のコマンドを実行します。

```bash
python test_reader.py
```

次のような出力が表示されるはずです。

```
First stock: Stock('AA', 100, 32.2)
First stock as dict: {'name': 'AA', 'shares': 100, 'price': 32.2}
First stock from direct parser: {'name': 'AA', 'shares': 100, 'price': 32.2}
```

この出力が表示されれば、リファクタリングしたコードが正しく動作していることを意味します。元の関数とパーサーの直接使用の両方が、期待される結果を生成しています。
