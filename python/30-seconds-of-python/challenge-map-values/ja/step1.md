# 辞書の値をマッピングする

## 問題

`map_values(obj, fn)` という関数を書きなさい。この関数は、辞書 `obj` と関数 `fn` を引数として取り、元の辞書と同じキーを持ち、各値に対して提供された関数を実行することで生成された値を持つ新しい辞書を返します。

## 例

```python
users = {
  'fred': { 'user': 'fred', 'age': 40 },
  'pebbles': { 'user': 'pebbles', 'age': 1 }
}
map_values(users, lambda u : u['age']) # {'fred': 40, 'pebbles': 1}
```

## 制約

- この関数は、要件を満たす任意の辞書と関数に対して機能する必要があります。
- この関数は、元の辞書を変更してはなりません。
