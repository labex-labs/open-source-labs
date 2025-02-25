# enumerate() 関数

`enumerate` 関数は、反復処理に追加のカウンタ値を付加します。

```python
names = ['Elwood', 'Jake', 'Curtis']
for i, name in enumerate(names):
    # i = 0 のとき name = 'Elwood' でループ
    # i = 1 のとき name = 'Jake'
    # i = 2 のとき name = 'Curtis'
```

一般的な形式は `enumerate(sequence [, start = 0])` です。`start` は省略可能です。`enumerate()` を使用する良い例は、ファイルを読み取りながら行番号を追跡することです。

```python
with open(filename) as f:
    for lineno, line in enumerate(f, start=1):
     ...
```

結局のところ、`enumerate` は以下のようなショートカットに過ぎません。

```python
i = 0
for x in s:
    statements
    i += 1
```

`enumerate` を使用すると、入力が少なくなり、わずかに高速に実行されます。
