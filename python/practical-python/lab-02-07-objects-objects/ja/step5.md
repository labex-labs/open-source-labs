# 識別と参照

2 つの値がまったく同じオブジェクトであるかどうかを確認するには、`is`演算子を使用します。

```python
>>> a = [1,2,3]
>>> b = a
>>> a is b
True
>>>
```

`is`は、オブジェクト識別（整数）を比較します。識別は`id()`を使用して取得できます。

```python
>>> id(a)
3588944
>>> id(b)
3588944
>>>
```

注：オブジェクトをチェックする際には、ほとんどの場合`==`を使用する方が良いです。`is`の動作はしばしば予期しない場合があります。

```python
>>> a = [1,2,3]
>>> b = a
>>> c = [1,2,3]
>>> a is b
True
>>> a is c
False
>>> a == c
True
>>>
```
