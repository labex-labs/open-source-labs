# リストの右端の要素を削除する

## 問題

`drop_right(a, n = 1)` という関数を書きなさい。この関数は、リスト `a` とオプションの整数 `n` を受け取り、リスト `a` の右端から `n` 個の要素を削除した新しいリストを返します。`n` が指定されない場合、関数はリストから最後の要素のみを削除する必要があります。

## 例

```python
drop_right([1, 2, 3]) # [1, 2]
drop_right([1, 2, 3], 2) # [1]
drop_right([1, 2, 3], 42) # []
```
