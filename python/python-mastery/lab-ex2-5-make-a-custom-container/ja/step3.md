# 方向を変える（列方向に）

データの見方を変えることで、多くのメモリを節約できることがよくあります。たとえば、この関数を使ってすべてのバスデータを列に読み込むとどうなるでしょうか。

```python
# readrides.py

...

def read_rides_as_columns(filename):
    '''
    バスの乗車データを4つのリストに読み込み、列を表す
    '''
    routes = []
    dates = []
    daytypes = []
    numrides = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # ヘッダーをスキップ
        for row in rows:
            routes.append(row[0])
            dates.append(row[1])
            daytypes.append(row[2])
            numrides.append(int(row[3]))
    return dict(routes=routes, dates=dates, daytypes=daytypes, numrides=numrides)
```

理論的には、この関数は多くのメモリを節約するはずです。試してみる前に分析してみましょう。

まず、データファイルには577563行のデータが含まれており、各行には4つの値が含まれています。各行を辞書として格納する場合、それらの辞書のサイズは最小で240バイトです。

```python
>>> nrows = 577563     # 元のファイルの行数
>>> nrows * 240
138615120
>>>
```

つまり、辞書自体だけで138MBになります。これには辞書に実際に格納されている値は含まれていません。

列方向に切り替えることで、データは4つの別々のリストに格納されます。各リストは項目ごとに8バイトのポインタを格納する必要があります。ですから、リストの要件の概算は次のようになります：

```python
>>> nrows * 4 * 8
18482016
>>>
```

これはリストのオーバーヘッドで約18MBです。したがって、列方向に切り替えることで、辞書に格納する必要のあるすべての余分な情報を削除することで、約120MBのメモリを節約できます。

この関数を使ってバスデータを読み込み、メモリ使用量を見てみましょう。

```python
>>> import tracemalloc
>>> tracemalloc.start()
>>> columns = read_rides_as_columns('ctabus.csv')
>>> tracemalloc.get_traced_memory()
... 結果を見る...
>>>
```

結果は、上の概算計算からの予想通りのメモリ節約を反映していますか？
