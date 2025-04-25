# 関数をより柔軟にする

現在、私たちの関数はファイル名で指定されたファイルからの読み取りに限定されています。これは関数の使い勝手を制限しています。プログラミングでは、関数をより柔軟にして、さまざまなタイプの入力を扱えるようにすることが多くの場合有益です。私たちの場合、関数がファイルオブジェクトや他のソースなど、行を生成する任意の反復可能オブジェクトで動作するようになれば素晴らしいです。これにより、圧縮ファイルや他のデータストリームからの読み取りなど、より多くのシナリオでこれらの関数を使用できるようになります。

この柔軟性を実現するためにコードをリファクタリングしましょう。

1. `reader.py` ファイルを開きます。新しい関数を追加するためにこのファイルを修正します。これらの新しい関数により、コードがさまざまなタイプの反復可能オブジェクトで動作するようになります。追加する必要があるコードは次のとおりです。

```python
# reader.py

import csv

def csv_as_dicts(lines, types):
    '''
    反復可能オブジェクトからの CSV データを辞書のリストに解析する

    引数：
        lines: CSV 行を生成する反復可能オブジェクト
        types: 各列の型変換関数のリスト

    戻り値：
        CSV 行のデータを含む辞書のリスト
    '''
    records = []
    rows = csv.reader(lines)
    headers = next(rows)
    for row in rows:
        record = { name: func(val)
                  for name, func, val in zip(headers, types, row) }
        records.append(record)
    return records

def csv_as_instances(lines, cls):
    '''
    反復可能オブジェクトからの CSV データをクラスインスタンスのリストに解析する

    引数：
        lines: CSV 行を生成する反復可能オブジェクト
        cls: インスタンスを作成するクラス

    戻り値：
        CSV 行のデータを含むクラスインスタンスのリスト
    '''
    records = []
    rows = csv.reader(lines)
    headers = next(rows)
    for row in rows:
        record = cls.from_row(row)
        records.append(record)
    return records

def read_csv_as_dicts(filename, types):
    '''
    CSV データを、オプションで型変換を行った辞書のリストに読み込む

    引数：
        filename: CSV ファイルへのパス
        types: 各列の型変換関数のリスト

    戻り値：
        CSV ファイルのデータを含む辞書のリスト
    '''
    with open(filename) as file:
        return csv_as_dicts(file, types)

def read_csv_as_instances(filename, cls):
    '''
    CSV データをクラスインスタンスのリストに読み込む

    引数：
        filename: CSV ファイルへのパス
        cls: インスタンスを作成するクラス

    戻り値：
        CSV ファイルのデータを含むクラスインスタンスのリスト
    '''
    with open(filename) as file:
        return csv_as_instances(file, cls)
```

コードをどのようにリファクタリングしたかを詳しく見てみましょう。

1. より汎用的な 2 つの関数 `csv_as_dicts()` と `csv_as_instances()` を作成しました。これらの関数は、CSV 行を生成する任意の反復可能オブジェクトで動作するように設計されています。これは、ファイル名で指定されたファイルだけでなく、さまざまなタイプの入力ソースを扱えることを意味します。
2. `read_csv_as_dicts()` と `read_csv_as_instances()` を再実装して、これらの新しい関数を使用するようにしました。これにより、ファイル名でファイルから読み取る元の機能は引き続き利用可能ですが、より柔軟な関数をベースに構築されるようになりました。
3. このアプローチは、既存のコードとの後方互換性を維持します。つまり、古い関数を使用していたコードは引き続き期待どおりに動作します。同時に、ライブラリはさまざまなタイプの入力ソースを扱えるようになるため、より柔軟になります。
4. では、これらの新しい関数をテストしましょう。`test_reader_flexibility.py` という名前のファイルを作成し、以下のコードを追加します。このコードは、さまざまなタイプの入力ソースで新しい関数をテストします。

```python
# test_reader_flexibility.py

import reader
import stock
import gzip

# 通常のファイルを開くテスト
with open('portfolio.csv') as file:
    portfolio = reader.csv_as_dicts(file, [str, int, float])
    print("First item from open file:", portfolio[0])

# 圧縮されたファイルを開くテスト
with gzip.open('portfolio.csv.gz', 'rt') as file:  # 'rt' はテキスト読み取りを意味する
    portfolio = reader.csv_as_instances(file, stock.Stock)
    print("\nFirst item from gzipped file:", portfolio[0])

# 後方互換性のテスト
portfolio = reader.read_csv_as_dicts('portfolio.csv', [str, int, float])
print("\nFirst item using backward compatible function:", portfolio[0])
```

3. テストファイルを作成した後、ターミナルからテストスクリプトを実行する必要があります。ターミナルを開き、`test_reader_flexibility.py` ファイルがあるディレクトリに移動します。次に、以下のコマンドを実行します。

```bash
python test_reader_flexibility.py
```

出力は次のようになるはずです。

```
First item from open file: {'name': 'AA', 'shares': 100, 'price': 32.2}

First item from gzipped file: Stock('AA', 100, 32.2)

First item using backward compatible function: {'name': 'AA', 'shares': 100, 'price': 32.2}
```

この出力は、関数が後方互換性を維持しながら、さまざまなタイプの入力ソースで動作することを確認しています。リファクタリングされた関数は、以下のソースからのデータを処理できます。

- `open()` で開かれた通常のファイル
- `gzip.open()` で開かれた圧縮ファイル
- テキスト行を生成する他の任意の反復可能オブジェクト

これにより、コードははるかに柔軟になり、さまざまなシナリオで使用しやすくなります。
