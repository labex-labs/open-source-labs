# テキストの基本的なメモリ使用量

このデータファイルを扱うために必要なメモリのベースラインを取得しましょう。まず、Pythonを再起動して、非常に単純な実験を行ってみましょう。つまり、ファイルを取得してそのデータを単一の文字列に格納するだけです。

```python
>>> # --- RESTART
>>> import tracemalloc
>>> f = open('ctabus.csv')
>>> tracemalloc.start()
>>> data = f.read()
>>> len(data)
12361039
>>> current, peak = tracemalloc.get_traced_memory()
>>> current
12369664
>>> peak
24730766
>>>
```

あなたの結果は多少異なるかもしれませんが、12MB前後の現在のメモリ使用量と24MBのピークを見るはずです。

代わりに、ファイル全体を文字列のリストに読み込むとどうなりますか？Pythonを再起動してこれを試してみましょう。

```python
>>> # --- RESTART
>>> import tracemalloc
>>> f = open('/home/labex/project/ctabus.csv')
>>> tracemalloc.start()
>>> lines = f.readlines()
>>> len(lines)
577564
>>> current, peak = tracemalloc.get_traced_memory()
>>> current
45828030
>>> peak
45867371
>>>
```

メモリ使用量が大幅に増えて40-50MBの範囲に上がるはずです。考えるポイント：その余分なオーバーヘッドの原因は何か？
