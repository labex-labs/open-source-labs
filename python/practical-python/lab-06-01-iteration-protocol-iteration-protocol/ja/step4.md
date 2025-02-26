# 演習6.1: 反復処理の例示

次のリストを作成します。

```python
a = [1,9,4,25,16]
```

このリストを手動で反復処理します。イテレータを取得するために `__iter__()` を呼び出し、連続する要素を取得するために `__next__()` メソッドを呼び出します。

```python
>>> i = a.__iter__()
>>> i
<listiterator object at 0x64c10>
>>> i.__next__()
1
>>> i.__next__()
9
>>> i.__next__()
4
>>> i.__next__()
25
>>> i.__next__()
16
>>> i.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>>
```

組み込み関数 `next()` は、イテレータの `__next__()` メソッドを呼び出すためのショートカットです。ファイルで試してみましょう。

```python
>>> f = open('portfolio.csv')
>>> f.__iter__()    # 注: これはファイル自体を返します
<_io.TextIOWrapper name='portfolio.csv' mode='r' encoding='UTF-8'>
>>> next(f)
'name,shares,price\n'
>>> next(f)
'"AA",100,32.20\n'
>>> next(f)
'"IBM",50,91.10\n'
>>>
```

`next(f)` を繰り返し呼び出して、ファイルの末尾に達するまで見てください。何が起こるか見てみましょう。
