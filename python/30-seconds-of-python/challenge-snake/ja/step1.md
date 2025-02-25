# スネークケース文字列

## 問題

`snake` という名前の Python 関数を書きましょう。この関数は文字列引数を受け取り、その文字列をスネークケースに変換して返します。関数は以下の手順を実行する必要があります。

1. `re.sub()` を使って文字列内のすべての単語をマッチさせ、`str.lower()` を使ってそれらを小文字に変換します。
2. `re.sub()` を使って `-` 文字をすべてスペースに置き換えます。
3. 最後に、`str.join()` を使ってすべての単語を `_` を区切り文字として結合します。

あなたの関数は、大文字と小文字の両方の文字、スペース、ハイフン、アンダースコアが混在した文字列を処理できる必要があります。

## 例

```python
snake('camelCase') # 'camel_case'
snake('some text') # 'some_text'
snake('some-mixed_string With spaces_underscores-and-hyphens')
# 'some_mixed_string_with_spaces_underscores_and_hyphens'
snake('AllThe-small Things') # 'all_the_small_things'
```
