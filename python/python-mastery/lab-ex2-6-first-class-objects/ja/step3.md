# メモリの再考

CTAバスデータでは、181の一意のバス路線があることがわかりました。

```python
>>> routes = { row['route'] for row in rows }
>>> len(routes)
181
>>>
```

質問：乗車データには、いくつの一意の路線文字列オブジェクトが含まれていますか？路線のセットを作成する代わりに、オブジェクトIDのセットを作成しましょう。

```python
>>> routeids = { id(row['route']) for row in rows }
>>> len(routeids)
542305
>>>
```

少し考えてみてください。一意の路線名は181個だけですが、辞書の結果のリストには542305個の異なる路線文字列が含まれています。多分、少しのキャッシングやオブジェクトの再利用でこれを修正できるかもしれません。実際、Pythonには文字列をキャッシングするために使用できる関数 `sys.intern()` があります。たとえば：

```python
>>> a = 'hello world'
>>> b = 'hello world'
>>> a is b
False
>>> import sys
>>> a = sys.intern(a)
>>> b = sys.intern(b)
>>> a is b
True
>>>
```

Pythonを再起動してこれを試してみましょう。

````python
>>> # ------------------ RESTART ---------```
>>> import tracemalloc
>>> tracemalloc.start()
>>> from sys import intern
>>> import reader
>>> rows = reader.read_csv_as_dicts('ctabus.csv', [intern, str, str, int])
>>> routeids = { id(row['route']) for row in rows }
>>> len(routeids)
181
>>>
````

メモリ使用量を見てみましょう。

```python
>>> tracemalloc.get_traced_memory()
... 結果を見る...
>>>
```

メモリはかなり減少するはずです。観察：日付に関してもたくさんの繰り返しがあります。日付文字列をキャッシングするとどうなりますか？

````python
>>> # ------------------ RESTART ---------```
>>> import tracemalloc
>>> tracemalloc.start()
>>> from sys import intern
>>> import reader
>>> rows = reader.read_csv_as_dicts('ctabus.csv', [intern, intern, str, int])
>>> tracemalloc.get_traced_memory()
... 結果を見る...
>>>
````
