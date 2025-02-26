# タプルのリスト

実際のところ、データをリストに読み込み、各行を他のデータ構造に変換することがあります。ここに、`csv` モジュールを使ってファイル全体をタプルのリストに読み込む `readrides.py` プログラムがあります。

```python
# readrides.py

import csv

def read_rides_as_tuples(filename):
    '''
    バス乗車データをタプルのリストとして読み込む
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # ヘッダーをスキップ
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = (route, date, daytype, rides)
            records.append(record)
    return records

if __name__ == '__main__':
    import tracemalloc
    tracemalloc.start()
    rows = read_rides_as_tuples('/home/labex/project/ctabus.csv')
    print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())
```

`python3 -i readrides.py` を使ってこのプログラムを実行し、`rows` の結果の内容を見てみましょう。このようなタプルのリストが得られるはずです。

```python
>>> len(rows)
577563
>>> rows[0]
('3', '01/01/2001', 'U', 7354)
>>> rows[1]
('4', '01/01/2001', 'U', 9288)
```

得られたメモリ使用量を見てみましょう。それは2つ目のステップよりも大幅に高くなるはずです。
