# 基本的な CSV リーダー関数の作成

まず、CSV データを読み取るための 2 つの基本的な関数を持つ `reader.py` ファイルを作成しましょう。これらの関数は、データを辞書やクラスインスタンスに変換するなど、さまざまな方法で CSV ファイルを扱うのに役立ちます。

まず、CSV ファイルとは何かを理解する必要があります。CSV は Comma-Separated Values（カンマ区切り値）の略です。これは、表形式のデータを格納するために使用される単純なファイル形式で、各行が 1 つの行を表し、各行の値はカンマで区切られています。

では、`reader.py` ファイルを作成しましょう。以下の手順に従ってください。

1. コードエディタを開き、`/home/labex/project` ディレクトリに `reader.py` という名前の新しいファイルを作成します。ここで、CSV データを読み取る関数を書きます。

2. `reader.py` に以下のコードを追加します。

```python
# reader.py

import csv

def read_csv_as_dicts(filename, types):
    '''
    CSV データを、オプションで型変換を行った辞書のリストに読み込む

    引数:
        filename: CSV ファイルへのパス
        types: 各列の型変換関数のリスト

    戻り値:
        CSV ファイルのデータを含む辞書のリスト
    '''
    records = []
    with open(filename) as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            record = { name: func(val)
                       for name, func, val in zip(headers, types, row) }
            records.append(record)
    return records

def read_csv_as_instances(filename, cls):
    '''
    CSV データをクラスインスタンスのリストに読み込む

    引数:
        filename: CSV ファイルへのパス
        cls: インスタンスを作成するクラス

    戻り値:
        CSV ファイルのデータを含むクラスインスタンスのリスト
    '''
    records = []
    with open(filename) as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            record = cls.from_row(row)
            records.append(record)
    return records
```

`read_csv_as_dicts` 関数では、まず `open` 関数を使用して CSV ファイルを開きます。次に、`csv.reader` を使用してファイルを 1 行ずつ読み取ります。`next(rows)` 文は、通常ヘッダーが含まれるファイルの最初の行を読み取ります。その後、残りの行を反復処理します。各行について、キーがヘッダーで、値が行内の対応する値である辞書を作成し、`types` リストを使用してオプションの型変換を行います。

`read_csv_as_instances` 関数も似ていますが、辞書を作成する代わりに、指定されたクラスのインスタンスを作成します。この関数は、クラスにデータの行からインスタンスを作成できる `from_row` という静的メソッドがあることを前提としています。

3. これらの関数が正しく動作することを確認するためにテストしましょう。以下のコードを持つ `test_reader.py` という名前の新しいファイルを作成します。

```python
# test_reader.py

import reader
import stock

# CSV を辞書として読み取るテスト
portfolio_dicts = reader.read_csv_as_dicts('portfolio.csv', [str, int, float])
print("First portfolio item as dictionary:", portfolio_dicts[0])
print("Total items:", len(portfolio_dicts))

# CSV をクラスインスタンスとして読み取るテスト
portfolio_instances = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
print("\nFirst portfolio item as Stock instance:", portfolio_instances[0])
print("Total items:", len(portfolio_instances))
```

`test_reader.py` ファイルでは、先ほど作成した `reader` モジュールと `stock` モジュールをインポートします。次に、`portfolio.csv` という名前のサンプル CSV ファイルを使用して 2 つの関数を呼び出してテストします。ポートフォリオの最初のアイテムとアイテムの総数を出力し、関数が期待どおりに動作していることを確認します。

4. ターミナルからテストスクリプトを実行します。

```bash
python test_reader.py
```

出力は次のようになるはずです。

```
First portfolio item as dictionary: {'name': 'AA', 'shares': 100, 'price': 32.2}
Total items: 7

First portfolio item as Stock instance: Stock('AA', 100, 32.2)
Total items: 7
```

これにより、2 つの関数が正しく動作していることが確認されます。最初の関数は、CSV データを適切な型変換を行った辞書のリストに変換し、2 番目の関数は、指定されたクラスの静的メソッドを使用してクラスインスタンスを作成します。

次のステップでは、これらの関数をリファクタリングして、ファイル名だけでなく、任意の反復可能なデータソースで動作するようにし、より柔軟にします。
