# 省略可能な引数にはキーワード引数を使うことを推奨

これらの2つの異なる呼び出しスタイルを比較してみましょう。

```python
parse_data(data, False, True) #?????

parse_data(data, ignore_errors=True)
parse_data(data, debug=True)
parse_data(data, debug=True, ignore_errors=True)
```

ほとんどの場合、キーワード引数はコードの明確さを向上させます。特に、フラグとして機能する引数や省略可能な機能に関連する引数の場合です。
