# スネークケースの文字列

文字列（string）を引数として受け取り、その文字列をスネークケース（snake case）に変換したものを返すPython関数 `snake` を作成してください。この関数は以下の手順を実行する必要があります。

1. `re.sub()` を使用して文字列内のすべての単語をマッチングし、`str.lower()` を使用して小文字に変換します。
2. `re.sub()` を使用して、すべての `-` 文字をスペースに置き換えます。
3. 最後に、`str.join()` を使用して、すべての単語を `_` を区切り文字として結合します。

あなたの関数は、大文字と小文字が混在した文字列、スペース、ハイフン、アンダースコアを含む文字列を処理できる必要があります。

```python
from re import sub

def snake(s):
  return '_'.join(
    sub('([A-Z][a-z]+)', r' \1',
    sub('([A-Z]+)', r' \1',
    s.replace('-', ' '))).split()).lower()
```

```python
snake('camelCase') # 'camel_case'
snake('some text') # 'some_text'
snake('some-mixed_string With spaces_underscores-and-hyphens')
# 'some_mixed_string_with_spaces_underscores_and_hyphens'
snake('AllThe-small Things') # 'all_the_small_things'
```
