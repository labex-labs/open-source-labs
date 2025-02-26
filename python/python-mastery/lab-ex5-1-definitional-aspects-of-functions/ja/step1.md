# 準備

演習2.6では、CSVを辞書のリストに読み込む関数を持つ`reader.py`モジュールを書きました。たとえば：

```python
>>> import reader
>>> port = reader.read_csv_as_dicts('portfolio.csv', [str,int,float])
>>>
```

後で、演習3.3でインスタンスと共に動作するようにコードを拡張しました：

```python
>>> import reader
>>> from stock import Stock
>>> port = reader.read_csv_as_instances('portfolio.csv', Stock)
>>>
```

最終的に、演習3.7ではコードが継承を含むクラスのコレクションにリファクタリングされました。ただし、コードはかなり複雑で入り組んでいます。
