# import文の使用

以前の演習では、`pcost.py`と`stock.py`の2つのプログラムを作成しました。`import`文を使用してこれらのプログラムを読み込み、その機能を使用します。

```python
>>> import pcost
44671.15
>>> pcost.portfolio_cost('portfolio2.dat')
19908.75
>>> from stock import Stock
>>> s = Stock('GOOG', 100, 490.10)
>>> s.name
'GOOG'
>>> s.cost()
49010.0
>>>
```

上記の文が機能しない場合は、プログラムを奇妙なディレクトリに配置している可能性があります。Pythonをファイルと同じディレクトリで実行していること、またはそのディレクトリが`sys.path`に含まれていることを確認してください。
