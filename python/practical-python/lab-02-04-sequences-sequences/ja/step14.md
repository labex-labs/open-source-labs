# 演習 2.15: enumerate() の実用的な例

ファイル `missing.csv` には株式ポートフォリオのデータが含まれていますが、一部の行に欠損データがあります。`enumerate()` を使って、`pcost.py` プログラムを修正して、入力が不適切な場合に警告メッセージとともに行番号を表示するようにしましょう。

```python
>>> cost = portfolio_cost('/home/labex/project/missing.csv')
Row 4: Couldn't convert: ['MSFT', '', '51.23']
Row 7: Couldn't convert: ['IBM', '', '70.44']
>>>
```

これを行うには、コードのいくつかの部分を変更する必要があります。

```python
...
for rowno, row in enumerate(rows, start=1):
    try:
     ...
    except ValueError:
        print(f'Row {rowno}: Bad row: {row}')
```
