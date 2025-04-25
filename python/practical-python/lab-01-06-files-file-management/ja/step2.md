# ファイルデータの読み取りに関する一般的な慣用句

文字列を使ってファイル全体を一度に読み取る。

```python
with open('foo.txt', 'rt') as file:
    data = file.read()
    # `data` は `foo.txt` のすべてのテキストが含まれた文字列です
```

イテレーションを使ってファイルを 1 行ずつ読み取る。

```python
with open(filename, 'rt') as file:
    for line in file:
        # 行を処理する
```
