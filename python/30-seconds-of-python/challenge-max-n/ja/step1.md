# N 個の最大要素チャレンジ

## 問題

`max_n(lst, n = 1)` という関数を書きましょう。この関数は、リスト `lst` とオプションの整数 `n` を引数として受け取り、与えられたリストからの `n` 個の最大要素のリストを返します。`n` が指定されない場合、関数はリストの最大要素を含むリストを返す必要があります。`n` がリストの長さ以上の場合、関数は降順にソートされた元のリストを返す必要があります。

あなたのタスクは、`max_n()` 関数を実装することです。

## 例

```python
max_n([1, 2, 3]) # [3]
max_n([1, 2, 3], 2) # [3, 2]
max_n([1, 2, 3, 4, 5], 3) # [5, 4, 3]
max_n([1, 2, 3, 4, 5], 6) # [5, 4, 3, 2, 1]
```
