# 文字列の最初の文字を小文字にする

文字列`s`を受け取り、最初の文字を小文字にした新しい文字列を返す関数`decapitalize(s, upper_rest = False)`を書きます。この関数は、オプションのパラメータ`upper_rest`も持ち、これが`True`に設定されている場合、文字列の残りを大文字に変換します。

```python
def decapitalize(s, upper_rest = False):
  return ''.join([s[:1].lower(), (s[1:].upper() if upper_rest else s[1:])])
```

```python
decapitalize('FooBar') # 'fooBar'
decapitalize('FooBar', True) # 'fOOBAR'
```
