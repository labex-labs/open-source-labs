# 演習6.15: コードの簡略化

ジェネレータ式は、小さなジェネレータ関数の便利な代替手段となることがよくあります。たとえば、次のような関数を書く代わりに：

```python
def filter_symbols(rows, names):
    for row in rows:
        if row['name'] in names:
            yield row
```

次のようなコードを書くことができます：

```python
rows = (row for row in rows if row['name'] in names)
```

`ticker.py` プログラムを修正して、適切にジェネレータ式を使用するようにします。
