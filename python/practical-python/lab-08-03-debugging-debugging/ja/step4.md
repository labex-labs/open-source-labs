# print を使ったデバッグ

`print()` によるデバッグは非常に一般的です。

**ヒント：`repr()` を使うことを確認しましょう。**

```python
def spam(x):
    print('DEBUG:', repr(x))
 ...
```

`repr()` は値の正確な表現を表示します。見やすい印刷出力ではありません。

```python
>>> from decimal import Decimal
>>> x = Decimal('3.4')
# `repr` なし
>>> print(x)
3.4
# `repr` あり
>>> print(repr(x))
Decimal('3.4')
>>>
```
