# 大量のメモリを節約する

演習 2.1 では、CTA バスデータを辞書のリストに読み込む関数 `read_rides_as_dicts()` を書きました。これを使用するには大量のメモリが必要です。たとえば、ルート 22 のバスが最も多く乗車した日を見つけてみましょう：

```python
>>> import tracemalloc
>>> tracemalloc.start()
>>> import readrides
>>> rows = readrides.read_rides_as_dicts('ctabus.csv')
>>> rt22 = [row for row in rows if row['route'] == '22']
>>> max(rt22, key=lambda row: row['rides'])
{'date': '06/11/2008', 'route': '22', 'daytype': 'W', 'rides': 26896}
>>> tracemalloc.get_traced_memory()
... 結果を見る。おおよそ220MB程度になるはず
>>>
```

次に、ジェネレータを含む例を試してみましょう。Python を再起動してこれを試してみましょう：

```python
>>> # RESTART
>>> import tracemalloc
>>> tracemalloc.start()
>>> import csv
>>> f = open('ctabus.csv')
>>> f_csv = csv.reader(f)
>>> headers = next(f_csv)
>>> rows = (dict(zip(headers,row)) for row in f_csv)
>>> rt22 = (row for row in rows if row['route'] == '22')
>>> max(rt22, key=lambda row: int(row['rides']))
{'date': '06/11/2008', 'route': '22', 'daytype': 'W', 'rides': 26896}
>>> tracemalloc.get_traced_memory()
... 結果を見る。以前よりはるかに小さくなるはず
>>>
```

ここでは、辞書のシーケンスとして保存されているかのように、実際にはすべてのデータセットを処理しました。しかし、実際に辞書のリストを作成して保存することは一度も行っていません。すべての問題をこのように構造化できるわけではありませんが、データを反復的に処理できる場合、ジェネレータ式を使うことで大量のメモリを節約できます。
