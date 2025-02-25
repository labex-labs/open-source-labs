# 一致する値を見つける

## 問題

`find(lst, fn)` という関数を書きます。この関数は、リスト `lst` とテスト関数 `fn` を引数として受け取ります。この関数は、`fn` が `True` を返す `lst` の最初の要素の値を返す必要があります。もし要素がテスト関数を満たさなければ、関数は `None` を返す必要があります。

## 例

```python
find([1, 2, 3, 4], lambda n: n % 2 == 1) # 1
find(['apple', 'banana', 'cherry'], lambda s: s.startswith('b')) # 'banana'
find([2, 4, 6, 8], lambda n: n % 2 == 1) # None
```
