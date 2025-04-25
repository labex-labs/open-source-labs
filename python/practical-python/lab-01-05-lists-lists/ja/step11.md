# 演習 1.23: ソート

リストをソートしたいですか？`sort()` メソッドを使ってみましょう。試してみましょう。

```python
>>> symlist.sort()
>>> symlist
['AA', 'AAPL', 'AIG', 'GOOG', 'HPQ', 'RHT', 'YHOO']
>>>
```

逆順にソートしたいですか？これを試してみましょう。

```python
>>> symlist.sort(reverse=True)
>>> symlist
['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA']
>>>
```

注：リストをソートすると、その内容が「その場で」変更されます。つまり、リストの要素が入れ替えられますが、結果として新しいリストは作成されません。
