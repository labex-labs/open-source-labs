# フレームのハッキング

前の部分についての1つの不満は、`__init__()` 関数が `locals()` への呼び出しが挿入されているため、今ではかなり奇妙に見えるということです。ただし、少しのスタックフレームのハッキングを行うことができれば、それを回避することができます。`_init()` 関数のこのバリアントを試してみてください。

```python
>>> import sys
>>> def _init():
        locs = sys._getframe(1).f_locals   # 呼び出し元の局所変数を取得
        self = locs.pop('self')
        for name, val in locs.items():
            setattr(self, name, val)
>>>
```

このコードでは、局所変数は呼び出し元のスタックフレームから抽出されます。以下は修正されたクラス定義です。

```python
>>> class Stock:
        def __init__(self, name, shares, price):
            _init()

>>> s = Stock('GOOG', 100, 490.1)
>>> s.name
'GOOG'
>>> s.shares
100
>>>
```

この時点で、おそらくあなたはかなり混乱していると感じているでしょう。そうです、あなたはちょうど別の関数のスタックフレームにアクセスしてその局所変数を調べる関数を書きました。
