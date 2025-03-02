# 準備

いくつかの新しい手法を使って、`Stock` クラスを最初から再作成します。演習5.4のユニットテストをすぐに手元に置いておいてください。それが必要になります。

関数を定義する場合、おそらくすでに知っていることですが、位置引数またはキーワード引数の組み合わせを使って呼び出すことができます。たとえば：

```python
>>> def foo(x, y, z):
        return x + y + z

>>> foo(1, 2, 3)
6
>>> foo(1, z=3, y=2)
6
>>>
```

また、シーケンスや辞書を \* と \*\* 構文を使って関数の引数として渡すこともできることもご存知かもしれません。たとえば：

```python
>>> args = (1, 2, 3)
>>> foo(*args)
6
>>> kwargs = {'y':2, 'z':3 }
>>> foo(1,**kwargs)
6
>>>
```

さらに、\* と \*\* 構文を使って任意の数の位置引数またはキーワード引数を受け付ける関数を書くこともできます。たとえば：

```python
>>> def foo(*args):
        print(args)

>>> foo(1,2)
(1, 2)
>>> foo(1,2,3,4,5)
(1, 2, 3, 4, 5)
>>> foo()
()
>>>
>>> def bar(**kwargs):
        print(kwargs)

>>> bar(x=1,y=2)
{'y': 2, 'x': 1}
>>> bar(x=1,y=2,z=3)
{'y': 2, 'x': 1, 'z': 3}
>>> bar()
{}
>>>
```

可変引数関数は、入力するコードの量を削減または単純化する手法として、時に便利です。この演習では、単純なデータ構造に対してその考え方を探求します。
