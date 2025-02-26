# 第3部 : リスト操作

最初の部分では、株価シンボルを含む文字列を扱いました。たとえば：

```python
>>> symbols = 'HPQ AAPL IBM MSFT YHOO  GOOG'
>>>
```

上記の変数を定義し、文字列の `split()` 操作を使用して名前のリストに分割します。

```python
>>> symlist = symbols.split()
>>> symlist
['HPQ', 'AAPL', 'IBM', 'MSFT', 'YHOO', 'GOOG' ]
>>>
```

## リスト要素の抽出と再割り当て

リストは配列のように機能し、数値インデックスを使って要素を参照して変更できます。いくつかの参照を試してみましょう。

```python
>>> symlist[0]
'HPQ'
>>> symlist[1]
'AAPL'
>>> symlist[-1]
'GOOG'
>>> symlist[-2]
'YHOO'
>>>
```

項目の再割り当てを試してみましょう。

```python
>>> symlist[2] = 'AIG'
>>> symlist
['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG' ]
>>>
```

## リスト項目のループ処理

`for` ループは、リストなどのシーケンス内のデータをループ処理します。次のループを入力し、何が起こるか見てみましょう。

```python
>>> for s in symlist:
        print('s =', s)

... 出力を見てください...
```

## メンバーシップテスト

`in` 演算子を使って、`'AIG'`、`'AA'`、および `'CAT'` がシンボルのリストに含まれているかどうかをチェックします。

```python
>>> 'AIG' in symlist
True
>>> 'AA' in symlist
False
>>>
```

## 項目の追加、挿入、削除

`append()` メソッドを使って、シンボル `'RHT'` を `symlist` の末尾に追加します。

```python
>>> symlist.append('RHT')
>>> symlist
['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG', 'RHT']
>>>
```

`insert()` メソッドを使って、シンボル `'AA'` をリストの2番目の項目として挿入します。

```python
>>> symlist.insert(1,'AA')
>>> symlist
['HPQ', 'AA', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG', 'RHT']
>>>
```

`remove()` メソッドを使って、`'MSFT'` をリストから削除します。

```python
>>> symlist.remove('MSFT')
>>> symlist
['HPQ', 'AA', 'AAPL', 'AIG', 'YHOO', 'GOOG', 'RHT']
```

項目が見つからない場合に何が起こるかを見るために、もう一度 `remove()` を呼び出してみましょう。

```python
>>> symlist.remove('MSFT')
... 何が起こるか見てください...
>>>
```

`index()` メソッドを使って、`'YHOO'` のリスト内の位置を見つけます。

```python
>>> symlist.index('YHOO')
4
>>> symlist[4]
'YHOO'
>>>
```

## リストのソート

リストをソートしたいですか？`sort()` メソッドを使ってみましょう。

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

## 任意のオブジェクトのリスト

リストには、他のリスト（たとえば、ネストされたリスト）を含む任意の種類のオブジェクトを含めることができます。これを試してみましょう。

```python
>>> nums = [101,102,103]
>>> items = [symlist, nums]
>>> items
[['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA'], [101, 102, 103]]
```

上記の出力に注目してください。`items` は2つの要素を持つリストです。各要素はリストです。

いくつかのネストされたリストの参照を試してみましょう。

```python
>>> items[0]
['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA']
>>> items[0][1]
'RHT'
>>> items[0][1][2]
'T'
>>> items[1]
[101, 102, 103]
>>> items[1][1]
102
>>>
```
