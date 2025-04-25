# 文字列を大文字にする

## 問題

文字列の先頭の文字を大文字にした新しい文字列を返す、`capitalize_string(s, lower_rest=False)` という Python 関数を書きます。この関数はオプションのパラメータ `lower_rest` を持ち、これが `True` に設定されている場合、文字列の残りの部分を小文字に変換します。

## 例

```python
capitalize_string('hello world') # 'Hello world'
capitalize_string('hello world', True) # 'Hello world'
```
