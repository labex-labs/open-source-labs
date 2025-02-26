# 演習3.17：ファイル名からファイルライクオブジェクトへ

これまでに、`parse_csv()` 関数を含む `fileparse.py` というファイルを作成しました。この関数は次のように機能しました。

```python
>>> import fileparse
>>> portfolio = fileparse.parse_csv('portfolio.csv', types=[str,int,float])
>>>
```

今のところ、この関数はファイル名を渡されることを期待しています。ただし、コードをより柔軟にすることができます。関数を修正して、任意のファイルライク/反復可能オブジェクトと動作するようにしましょう。たとえば：

```python
>>> import fileparse
>>> import gzip
>>> with gzip.open('portfolio.csv.gz', 'rt') as file:
...      port = fileparse.parse_csv(file, types=[str,int,float])
...
>>> lines = ['name,shares,price', 'AA,100,34.23', 'IBM,50,91.1', 'HPE,75,45.1']
>>> port = fileparse.parse_csv(lines, types=[str,int,float])
>>>
```

この新しいコードでは、以前と同じようにファイル名を渡すと何が起こりますか？

```python
>>> port = fileparse.parse_csv('portfolio.csv', types=[str,int,float])
>>> port
... 出力を見る（おそらく狂った出力になるはず）...
>>>
```

はい、注意が必要です。これを回避するためのセーフティチェックを追加できますか？
