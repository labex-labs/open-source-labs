# 演習 1.19: リスト要素の抽出と再割り当て

いくつかの参照を試してみましょう。

```python
>>> symlist[0]
'HPQ'
>>> symlist[1]
'AAPL'
>>> symlist[-1]
'GOOG'
>>> symlist[-2]
'DOA'
>>>
```

1 つの値を再割り当てしてみましょう。

```python
>>> symlist[2] = 'AIG'
>>> symlist
['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'DOA', 'GOOG']
>>>
```

いくつかのスライスを取ってみましょう。

```python
>>> symlist[0:3]
['HPQ', 'AAPL', 'AIG']
>>> symlist[-2:]
['DOA', 'GOOG']
>>>
```

空のリストを作成して、そこに項目を追加しましょう。

```python
>>> mysyms = []
>>> mysyms.append('GOOG')
>>> mysyms
['GOOG']
```

リストの一部を別のリストに再割り当てることができます。たとえば：

```python
>>> symlist[-2:] = mysyms
>>> symlist
['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG']
>>>
```

このようにすると、左辺のリスト (`symlist`) は右辺のリスト (`mysyms`) が収まるように適切にサイズ変更されます。たとえば、上の例では、`symlist` の最後の 2 つの項目が、リスト `mysyms` の 1 つの項目に置き換えられました。
