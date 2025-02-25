# 演習1.22: 項目の追加、挿入、削除

`append()` メソッドを使って、シンボル `'RHT'` を `symlist` の末尾に追加します。

```python
>>> symlist.append('RHT') # 'RHT' を追加
>>> symlist
['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG', 'RHT']
>>>
```

`insert()` メソッドを使って、シンボル `'AA'` をリストの2番目の項目として挿入します。

```python
>>> symlist.insert(1, 'AA') # 'AA' をリストの2番目の項目として挿入
>>> symlist
['HPQ', 'AA', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG', 'RHT']
>>>
```

`remove()` メソッドを使って、リストから `'MSFT'` を削除します。

```python
>>> symlist.remove('MSFT') # 'MSFT' を削除
>>> symlist
['HPQ', 'AA', 'AAPL', 'AIG', 'YHOO', 'GOOG', 'RHT']
>>>
```

リストの末尾に `'YHOO'` の重複エントリを追加します。

_注: リストに重複する値があるのは完全に正常です。_

```python
>>> symlist.append('YHOO') # 'YHOO' を追加
>>> symlist
['HPQ', 'AA', 'AAPL', 'AIG', 'YHOO', 'GOOG', 'RHT', 'YHOO']
>>>
```

`index()` メソッドを使って、リスト内の `'YHOO'` の最初の位置を見つけます。

```python
>>> symlist.index('YHOO') # 'YHOO' の最初のインデックスを見つける
4
>>> symlist[4]
'YHOO'
>>>
```

リスト内の `'YHOO'` が何回出現するか数えます:

```python
>>> symlist.count('YHOO')
2
>>>
```

最初に出現する `'YHOO'` を削除します。

```python
>>> symlist.remove('YHOO') # 最初に出現する 'YHOO' を削除
>>> symlist
['HPQ', 'AA', 'AAPL', 'AIG', 'GOOG', 'RHT', 'YHOO']
>>>
```

ご存知のように、項目のすべての出現を見つけたり削除したりするメソッドはありません。ただし、セクション2でこれを行うエレガントな方法を見ます。
