# C スタイルの書式設定

書式設定演算子`%`も使用できます。

```python
>>> 'The value is %d' % 3
'The value is 3'
>>> '%5d %-5d %10d' % (3,4,5)
'    3 4              5'
>>> '%0.2f' % (3.1415926,)
'3.14'
```

これには右辺に単一の項目またはタプルが必要です。書式コードもまた C 言語の`printf()`に基づいています。

_注：これはバイト文字列で利用可能な唯一の書式設定です。_

```python
>>> b'%s has %d messages' % (b'Dave', 37)
b'Dave has 37 messages'
>>> b'%b has %d messages' % (b'Dave', 37)  # %bは%sの代わりに使用できます
b'Dave has 37 messages'
>>>
```
