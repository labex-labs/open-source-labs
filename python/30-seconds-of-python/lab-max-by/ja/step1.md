# 関数に基づくリストの最大値を見つける

`max_by(lst, fn)` という関数を書きます。この関数は、リスト `lst` と関数 `fn` を引数として取ります。この関数は、提供された関数 `fn` を使って `lst` の各要素を別の値にマッピングし、その後最大値を返す必要があります。

```python
def max_by(lst, fn):
  return max(map(fn, lst))
```

```python
max_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda v : v['n']) # 8
```
