# リストの作成

ゼロからリストを作成する。

```python
records = []  # 初期の空のリスト

#.append() を使用して項目を追加する
records.append(('GOOG', 100, 490.10))
records.append(('IBM', 50, 91.3))
...
```

ファイルからレコードを読み取る場合の例。

```python
records = []  # 初期の空のリスト

with open('portfolio.csv', 'rt') as f:
    next(f) # ヘッダーをスキップする
    for line in f:
        row = line.split(',')
        records.append((row[0], int(row[1]), float(row[2])))
```
