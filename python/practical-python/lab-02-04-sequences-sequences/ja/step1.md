# シーケンスデータ型

Python には 3 つの「シーケンス」データ型があります。

- 文字列: `'Hello'`。文字列は文字のシーケンスです。
- リスト: `[1, 4, 5]`。
- タプル: `('GOOG', 100, 490.1)`。

すべてのシーケンスは順序付きで、整数でインデックス付けされ、長さを持っています。

```python
a = 'Hello'               # 文字列
b = [1, 4, 5]             # リスト
c = ('GOOG', 100, 490.1)  # タプル

# インデックス付けされた順序
a[0]                      # 'H'
b[-1]                     # 5
c[1]                      # 100

# シーケンスの長さ
len(a)                    # 5
len(b)                    # 3
len(c)                    # 3
```

シーケンスは複製できます: `s * n`。

```python
>>> a = 'Hello'
>>> a * 3
'HelloHelloHello'
>>> b = [1, 2, 3]
>>> b * 2
[1, 2, 3, 1, 2, 3]
>>>
```

同じ型のシーケンスは連結できます: `s + t`。

```python
>>> a = (1, 2, 3)
>>> b = (4, 5)
>>> a + b
(1, 2, 3, 4, 5)
>>>
>>> c = [1, 5]
>>> a + c
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate tuple (not "list") to tuple
```
