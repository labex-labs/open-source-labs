# 関数に基づく最大リスト値を見つける

## 問題

`max_by(lst, fn)` という関数を書きます。この関数は、リスト `lst` と関数 `fn` を引数として取ります。この関数は、提供された関数 `fn` を使って `lst` の各要素を別の値にマッピングし、その後最大値を返す必要があります。

## 例

```python
max_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda v : v['n']) # 8
```

## 制約

- リスト `lst` には少なくとも 1 つの要素が含まれます。
- 関数 `fn` は 1 つの引数を取り、値を返します。
