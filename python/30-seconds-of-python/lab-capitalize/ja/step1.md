# 文字列を大文字にする

文字列の先頭の文字を大文字にした新しい文字列を返す、`capitalize_string(s, lower_rest=False)` というPython関数を書きます。この関数はオプションのパラメータ `lower_rest` を持ち、これが `True` に設定されている場合、文字列の残りの部分を小文字に変換します。

```python
def capitalize(s, lower_rest = False):
  return ''.join([s[:1].upper(), (s[1:].lower() if lower_rest else s[1:])])
```

```python
capitalize('fooBar') # 'FooBar'
capitalize('fooBar', True) # 'Foobar'
```
