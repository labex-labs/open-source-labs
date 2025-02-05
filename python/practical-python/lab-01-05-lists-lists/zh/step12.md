# 练习1.24：将所有内容整合起来

想把一个字符串列表连接成一个字符串吗？像这样使用字符串的 `join()` 方法（注意：一开始看起来有点奇怪）。

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
