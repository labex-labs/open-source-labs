# 文字列変換用の特殊メソッド

オブジェクトには 2 種類の文字列表現があります。

```python
>>> from datetime import date
>>> d = date(2012, 12, 21)
>>> print(d)
2012-12-21
>>> d
datetime.date(2012, 12, 21)
>>>
```

`str()` 関数は、見やすい表示用の出力を作成するために使用されます。

```python
>>> str(d)
'2012-12-21'
>>>
```

`repr()` 関数は、プログラマー向けのより詳細な表現を作成するために使用されます。

```python
>>> repr(d)
'datetime.date(2012, 12, 21)'
>>>
```

これらの関数 `str()` と `repr()` は、クラス内の一対の特殊メソッドを使用して表示する文字列生成します。

```python
class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # `str()` と共に使用
    def __str__(self):
        return f'{self.year}-{self.month}-{self.day}'

    # `repr()` と共に使用
    def __repr__(self):
        return f'Date({self.year},{self.month},{self.day})'
```

_注: `__repr__()` の規約は、`eval()` に渡されたときに元のオブジェクトを再作成する文字列を返すことです。これが不可能な場合は、代わりに読みやすい表現を使用します。_
