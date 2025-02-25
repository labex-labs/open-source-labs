# 辞書をソートする

`sort_dict_by_value(d, reverse=False)` という名前の関数を作成します。この関数は辞書 `d` を受け取り、値に基づいてソートします。関数は、元の辞書と同じキーを持ち、値が昇順にソートされた新しい辞書を返す必要があります。`reverse` パラメータが `True` に設定されている場合、関数は辞書を降順にソートする必要があります。

この問題を解決するには、次の手順を辿ることができます。

1. `dict.items()` を使用して、`d` からタプル ペアのリストを取得します。
2. ラムダ関数と `sorted()` を使用してリストをソートします。
3. `dict()` を使用して、ソートされたリストを辞書に戻します。
4. `sorted()` の `reverse` パラメータを使用して、2番目の引数に基づいて辞書を逆順にソートします。

**⚠️ 注意:** 辞書の値は同じ型でなければなりません。

```python
def sort_dict_by_value(d, reverse = False):
  return dict(sorted(d.items(), key = lambda x: x[1], reverse = reverse))
```

```python
d = {'one': 1, 'three': 3, 'five': 5, 'two': 2, 'four': 4}
sort_dict_by_value(d) # {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
sort_dict_by_value(d, True)
# {'five': 5, 'four': 4, 'three': 3, 'two': 2, 'one': 1}
```
