# 既存の関数をリファクタリングする

ここでは、`convert_csv()` という名前の高階関数を作成しました。高階関数とは、他の関数を引数として受け取ったり、関数を結果として返したりする関数です。これは Python で非常に強力な概念であり、よりモジュール化され再利用可能なコードを書くのに役立ちます。このセクションでは、この高階関数を使って、元の関数 `csv_as_dicts()` と `csv_as_instances()` をリファクタリングします。リファクタリングとは、既存のコードの外部的な振る舞いを変えることなく、内部構造を改善するためにコードを再構築するプロセスで、例えばコードの重複を排除することが目的です。

まず、WebIDE で `reader.py` ファイルを開きましょう。以下のように関数を更新します。

1. まず、`csv_as_dicts()` 関数を置き換えます。この関数は、CSV データの行を辞書のリストに変換するために使用されます。以下が新しいコードです。

```python
def csv_as_dicts(lines, types, *, headers=None):
    '''
    Convert lines of CSV data into a list of dictionaries
    '''
    def dict_converter(headers, row):
        return {name: func(val) for name, func, val in zip(headers, types, row)}

    return convert_csv(lines, dict_converter, headers=headers)
```

このコードでは、`headers` と `row` を引数とする内部関数 `dict_converter` を定義しています。この関数は辞書内包表記を使って、キーがヘッダー名で、値が行内の値に対応する型変換関数を適用した結果である辞書を作成します。そして、`dict_converter` 関数を引数として `convert_csv()` 関数を呼び出します。

2. 次に、`csv_as_instances()` 関数を置き換えます。この関数は、CSV データの行を指定されたクラスのインスタンスのリストに変換するために使用されます。以下が新しいコードです。

```python
def csv_as_instances(lines, cls, *, headers=None):
    '''
    Convert lines of CSV data into a list of instances
    '''
    def instance_converter(headers, row):
        return cls.from_row(row)

    return convert_csv(lines, instance_converter, headers=headers)
```

このコードでは、`headers` と `row` を引数とする内部関数 `instance_converter` を定義しています。この関数は、指定されたクラス `cls` の `from_row` クラスメソッドを呼び出して、行からインスタンスを作成します。そして、`instance_converter` 関数を引数として `convert_csv()` 関数を呼び出します。

これらの関数をリファクタリングした後、期待通りに動作することを確認するためにテストする必要があります。これを行うには、Python シェルで以下のコマンドを実行します。

```bash
cd ~/project
python3 -i reader.py
```

`cd ~/project` コマンドは、現在の作業ディレクトリを `project` ディレクトリに変更します。`python3 -i reader.py` コマンドは、`reader.py` ファイルを対話モードで実行します。これは、ファイルの実行が終了した後も Python コードを続けて実行できることを意味します。

Python シェルが開いたら、以下のコードを実行してリファクタリングした関数をテストします。

```python
# Define a simple Stock class for testing
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @classmethod
    def from_row(cls, row):
        return cls(row[0], int(row[1]), float(row[2]))

    def __repr__(self):
        return f'Stock({self.name}, {self.shares}, {self.price})'

# Test csv_as_dicts
with open('portfolio.csv') as f:
    portfolio_dicts = csv_as_dicts(f, [str, int, float])
print("First dictionary:", portfolio_dicts[0])

# Test csv_as_instances
with open('portfolio.csv') as f:
    portfolio_instances = csv_as_instances(f, Stock)
print("First instance:", portfolio_instances[0])
```

このコードでは、まずテスト用に簡単な `Stock` クラスを定義しています。`__init__` メソッドは `Stock` インスタンスの属性を初期化します。`from_row` クラスメソッドは、CSV データの行から `Stock` インスタンスを作成します。`__repr__` メソッドは `Stock` インスタンスの文字列表現を提供します。

次に、`portfolio.csv` ファイルを開き、型変換関数のリストとともに `csv_as_dicts()` 関数に渡すことで、この関数をテストします。結果のリストの最初の辞書を出力します。

最後に、`portfolio.csv` ファイルを開き、`Stock` クラスとともに `csv_as_instances()` 関数に渡すことで、この関数をテストします。結果のリストの最初のインスタンスを出力します。

すべてが正しく動作していれば、以下のような出力が表示されるはずです。

```
First dictionary: {'name': 'AA', 'shares': 100, 'price': 32.2}
First instance: Stock(AA, 100, 32.2)
```

この出力は、リファクタリングした関数が正しく動作していることを示しています。同じ機能を維持しながら、コードの重複を成功裏に排除しました。

Python シェルを終了するには、`exit()` と入力するか、Ctrl+D を押します。
