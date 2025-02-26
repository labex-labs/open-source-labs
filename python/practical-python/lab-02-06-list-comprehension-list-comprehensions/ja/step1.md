# 新しいリストの作成

リスト内包表記は、シーケンスの各要素に演算を適用することで新しいリストを作成します。

```python
>>> a = [1, 2, 3, 4, 5]
>>> b = [2*x for x in a ]
>>> b
[2, 4, 6, 8, 10]
>>>
```

別の例：

```python
>>> names = ['Elwood', 'Jake']
>>> a = [name.lower() for name in names]
>>> a
['elwood', 'jake']
>>>
```

一般的な構文は：`[ <式> for <変数名> in <シーケンス> ]` です。
