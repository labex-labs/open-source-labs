# すべての一致するインデックスを見つける

引数としてリスト `lst` とテスト関数 `fn` を取り、`fn` が `True` を返す `lst` 内のすべての要素のインデックスのリストを返す関数 `find_index_of_all(lst, fn)` を書きなさい。

### 入力

- 整数のリスト `lst`
- 整数を入力として受け取り、ブール値を返すテスト関数 `fn`

### 出力

- `fn` が `True` を返す `lst` 内のすべての要素のインデックスを表す整数のリスト

```python
def find_index_of_all(lst, fn):
  return [i for i, x in enumerate(lst) if fn(x)]
```

```python
find_index_of_all([1, 2, 3, 4], lambda n: n % 2 == 1) # [0, 2]
```
