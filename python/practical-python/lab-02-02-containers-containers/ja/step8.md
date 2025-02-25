# セット

セットは、順序がなく、重複しない要素のコレクションです。

```python
tech_stocks = { 'IBM','AAPL','MSFT' }
# 別の構文
tech_stocks = set(['IBM', 'AAPL', 'MSFT'])
```

セットは、メンバーシップテストに便利です。

```python
>>> tech_stocks
set(['AAPL', 'IBM', 'MSFT'])
>>> 'IBM' in tech_stocks
True
>>> 'FB' in tech_stocks
False
>>>
```

セットは、重複削除にも便利です。

```python
names = ['IBM', 'AAPL', 'GOOG', 'IBM', 'GOOG', 'YHOO']

unique = set(names)
# unique = set(['IBM', 'AAPL','GOOG','YHOO'])
```

追加のセット演算：

```python
unique.add('CAT')        # 要素を追加する
unique.remove('YHOO')    # 要素を削除する

s1 = { 'a', 'b', 'c'}
s2 = { 'c', 'd' }
s1 | s2                 # セットの和集合 { 'a', 'b', 'c', 'd' }
s1 & s2                 # セットの積集合 { 'c' }
s1 - s2                 # セットの差集合 { 'a', 'b' }
```

これらの演習では、このコースの残りの部分で使用される主要なプログラムの1つを作成し始めます。`report.py` ファイルで作業してください。
