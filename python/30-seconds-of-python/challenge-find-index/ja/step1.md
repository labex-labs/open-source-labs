# 一致するインデックスを見つける

## 問題

引数としてリスト`lst`とテスト関数`fn`を取る関数`find_index(lst, fn)`を書きます。この関数は、`fn`が`True`を返す`lst`の最初の要素のインデックスを返す必要があります。

## 例

```python
find_index([1, 2, 3, 4], lambda n: n % 2 == 1) # 0
```
