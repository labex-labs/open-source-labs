# タプルを使った構造化データの操作

これまでは生のテキストデータの保存を扱ってきました。しかし、データ分析の際には、通常、データをより整理された構造化形式に変換する必要があります。これにより、様々な操作を行いやすくなり、データから洞察を得ることができます。このステップでは、`csv` モジュールを使ってデータをタプルのリストとして読み込む方法を学びます。タプルは、複数の値を保持できる Python のシンプルで便利なデータ構造です。

## タプルを使ったリーダー関数の作成

`/home/labex/project` ディレクトリに `readrides.py` という名前の新しいファイルを作成しましょう。このファイルには、CSV ファイルからデータを読み込み、タプルのリストとして保存するコードが含まれます。

```python
# readrides.py
import csv
import tracemalloc

def read_rides_as_tuples(filename):
    '''
    バスの乗車データをタプルのリストとして読み込む
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # ヘッダーをスキップする
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = (route, date, daytype, rides)
            records.append(record)
    return records

if __name__ == '__main__':
    tracemalloc.start()

    rows = read_rides_as_tuples('/home/labex/project/ctabus.csv')

    current, peak = tracemalloc.get_traced_memory()
    print(f'Number of records: {len(rows)}')
    print(f'First record: {rows[0]}')
    print(f'Second record: {rows[1]}')
    print(f'Memory Use: Current {current/1024/1024:.2f} MB, Peak {peak/1024/1024:.2f} MB')
```

このスクリプトは `read_rides_as_tuples` という関数を定義しています。以下はその処理の流れです。

1. `filename` パラメータで指定された CSV ファイルを開きます。これにより、ファイル内のデータにアクセスできます。
2. `csv` モジュールを使ってファイルの各行を解析します。`csv.reader` 関数は、行を個々の値に分割するのに役立ちます。
3. 各行から 4 つのフィールド（路線、日付、曜日タイプ、乗車人数）を抽出します。これらのフィールドはデータ分析に重要です。
4. 'rides' フィールドを整数に変換します。CSV ファイル内のデータは最初は文字列形式なので、計算には数値が必要です。
5. これら 4 つの値を持つタプルを作成します。タプルは不変であり、一度作成されると値を変更することはできません。
6. タプルを `records` というリストに追加します。このリストは CSV ファイルのすべてのレコードを保持します。

では、スクリプトを実行しましょう。ターミナルを開き、以下のコマンドを入力します。

```bash
python3 /home/labex/project/readrides.py
```

以下のような出力が表示されるはずです。

```
Number of records: 577563
First record: ('3', '01/01/2001', 'U', 7354)
Second record: ('4', '01/01/2001', 'U', 9288)
Memory Use: Current 89.12 MB, Peak 89.15 MB
```

前の例と比較すると、メモリ使用量が増加していることに注意してください。これにはいくつかの理由があります。

1. 現在、データを構造化形式（タプル）で保存しています。構造化データは通常、定義された組織構造を持つため、より多くのメモリを必要とします。
2. タプル内の各値は別々の Python オブジェクトです。Python オブジェクトにはオーバーヘッドがあり、これがメモリ使用量の増加に寄与します。
3. これらすべてのタプルを保持する追加のリスト構造があります。リストも要素を保存するためにメモリを占有します。

このアプローチの利点は、データが適切に構造化され、分析の準備ができていることです。各レコードの特定のフィールドにインデックスで簡単にアクセスできます。例えば：

```python
# タプル要素へのアクセスの例（試すには readrides.py ファイルに追加する）
first_record = rows[0]
route = first_record[0]
date = first_record[1]
daytype = first_record[2]
rides = first_record[3]
print(f"Route: {route}, Date: {date}, Day type: {daytype}, Rides: {rides}")
```

ただし、数値インデックスでデータにアクセスすることは常に直感的ではありません。特に多数のフィールドを扱う場合、どのインデックスがどのフィールドに対応するかを覚えるのは難しいことがあります。次のステップでは、コードをより読みやすく保守しやすくする他のデータ構造を探索します。
