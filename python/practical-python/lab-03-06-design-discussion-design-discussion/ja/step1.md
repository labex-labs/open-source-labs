# ファイル名と反復可能オブジェクト

同じ出力を返すこの2つのプログラムを比較しましょう。

```python
# ファイル名を指定する
def read_data(filename):
    records = []
    with open(filename) as f:
        for line in f:
           ...
            records.append(r)
    return records

d = read_data('file.csv')
```

```python
# 行を指定する
def read_data(lines):
    records = []
    for line in lines:
       ...
        records.append(r)
    return records

with open('file.csv') as f:
    d = read_data(f)
```

- これらの関数のどちらが好きですか？なぜですか？
- これらの関数のどちらがより柔軟ですか？
