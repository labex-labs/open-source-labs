# 辞書の作成

ゼロから辞書を作成する例。

```python
prices = {} # 初期の空の辞書

# 新しい項目を挿入する
prices['GOOG'] = 513.25
prices['CAT'] = 87.22
prices['IBM'] = 93.37
```

ファイルの内容から辞書を作成する例。

```python
prices = {} # 初期の空の辞書

with open('prices.csv', 'rt') as f:
    for line in f:
        row = line.split(',')
        prices[row[0]] = float(row[1])
```

注：`prices.csv` ファイルでこれを試すと、ほぼ機能することがわかります。ただし、末尾に空行があるため、コードがクラッシュします。それに対応するためのコードを修正する方法を考える必要があります（演習2.6を参照）。
