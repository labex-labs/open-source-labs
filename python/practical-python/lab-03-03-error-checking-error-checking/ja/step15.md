# 演習3.9：例外のキャッチ

あなたが書いた `parse_csv()` 関数は、ファイルの全体の内容を処理するために使用されます。しかし、現実の世界では、入力ファイルに破損、欠落、または汚染されたデータが含まれている可能性があります。この実験を試してみてください：

```python
>>> portfolio = parse_csv('missing.csv', types=[str, int, float])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "fileparse.py", line 36, in parse_csv
    row = [func(val) for func, val in zip(types, row)]
ValueError: invalid literal for int() with base 10: ''
>>>
```

`parse_csv()` 関数を修正して、レコード作成中に発生するすべての `ValueError` 例外をキャッチし、変換できない行に対して警告メッセージを表示するようにします。

メッセージには、行番号と失敗した理由に関する情報が含まれている必要があります。関数をテストするには、上記の `missing.csv` ファイルを読み取ってみてください。たとえば：

```python
>>> portfolio = parse_csv('missing.csv', types=[str, int, float])
Row 4: Couldn't convert ['MSFT', '', '51.23']
Row 4: Reason invalid literal for int() with base 10: ''
Row 7: Couldn't convert ['IBM', '', '70.44']
Row 7: Reason invalid literal for int() with base 10: ''
>>>
>>> portfolio
[{'name': 'AA','shares': 100, 'price': 32.2}, {'name': 'IBM','shares': 50, 'price': 91.1}, {'name': 'CAT','shares': 150, 'price': 83.44}, {'name': 'GE','shares': 95, 'price': 40.37}, {'name': 'MSFT','shares': 50, 'price': 65.1}]
>>>
```
