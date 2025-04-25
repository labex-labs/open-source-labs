# 演習 1.24: すべてを再構築する

文字列をリストとして受け取り、それらを 1 つの文字列に結合したいですか？このように文字列の `join()` メソッドを使います (注：最初は少々奇妙に見えます)。

```python
>>> a = ','.join(symlist)
>>> a
'YHOO,RHT,HPQ,GOOG,AIG,AAPL,AA'
>>> b = ':'.join(symlist)
>>> b
'YHOO:RHT:HPQ:GOOG:AIG:AAPL:AA'
>>> c = ''.join(symlist)
>>> c
'YHOORHTHPQGOOGAIGAAPLAA'
>>>
```
