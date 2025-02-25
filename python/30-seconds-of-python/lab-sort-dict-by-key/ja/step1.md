# キーで辞書をソートする

辞書 `d` を受け取り、キーでソートされた新しい辞書を返す関数 `sort_dict_by_key(d, reverse=False)` を書きます。この関数は、既定値が `False` のオプションパラメータ `reverse` を持つ必要があります。`reverse` が `True` の場合、辞書は逆順にソートされる必要があります。

```python
def sort_dict_by_key(d, reverse = False):
  return dict(sorted(d.items(), reverse = reverse))
```

```python
d = {'one': 1, 'three': 3, 'five': 5, 'two': 2, 'four': 4}
sort_dict_by_key(d) # {'five': 5, 'four': 4, 'one': 1, 'three': 3, 'two': 2}
sort_dict_by_key(d, True)
# {'two': 2, 'three': 3, 'one': 1, 'four': 4, 'five': 5}
```
