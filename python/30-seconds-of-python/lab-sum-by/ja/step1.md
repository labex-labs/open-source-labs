# 関数に基づくリストの合計

`sum_by(lst, fn)` という関数を書きます。この関数は、リスト `lst` と関数 `fn` を引数として取ります。この関数は、提供された関数を使ってリストの各要素をある値にマッピングし、その値の合計を返す必要があります。

```python
def sum_by(lst, fn):
  return sum(map(fn, lst))
```

```python
sum_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda v : v['n']) # 20
```
