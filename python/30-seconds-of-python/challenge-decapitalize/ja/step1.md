# 文字列の最初の文字を小文字にする

## 問題

文字列`s`を受け取り、最初の文字を小文字にした新しい文字列を返す関数`decapitalize(s, upper_rest = False)`を作成します。この関数は、オプションのパラメータ`upper_rest`も持ち、これが`True`に設定されている場合、文字列の残りの部分を大文字に変換します。

## 例

```python
decapitalize('FooBar') # 'fooBar'
decapitalize('FooBar', True) # 'fOOBAR'
```
