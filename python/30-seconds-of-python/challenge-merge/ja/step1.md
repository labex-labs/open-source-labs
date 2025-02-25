# リストをマージする

## 問題

`merge(*args, fill_value=None)` という名前の関数を書きましょう。この関数は 2 つ以上のリストを引数として受け取り、リストのリストを返します。関数は、入力リストそれぞれの要素を位置に基づいて結合する必要があります。あるリストが最長のリストより短い場合、関数は残りの要素に `fill_value` を使用する必要があります。`fill_value` が提供されない場合、デフォルト値は `None` にする必要があります。

あなたのタスクは、`merge()` 関数を実装することです。

## 例

```python
merge(['a', 'b'], [1, 2], [True, False]) # [['a', 1, True], ['b', 2, False]]
merge(['a'], [1, 2], [True, False]) # [['a', 1, True], [None, 2, False]]
merge(['a'], [1, 2], [True, False], fill_value = '_')
# [['a', 1, True], ['_', 2, False]]
```
