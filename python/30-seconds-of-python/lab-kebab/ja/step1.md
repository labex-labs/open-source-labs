# ケバブケースの文字列

`to_kebab_case(s)` という名前の Python 関数を書きましょう。この関数は文字列 `s` を入力として受け取り、その文字列をケバブケースのバージョンで返します。関数は次の手順を実行する必要があります。

1. 正規表現 `r"(_|-)+"` を使用して、`-` または `_` をすべてスペースに置き換えます。
2. 文字列内のすべての単語を一致させ、`str.lower()` を使って小文字に変換します。
3. すべての単語を `-` を区切り文字として結合します。

```python
from re import sub

def kebab(s):
  return '-'.join(
    sub(r"(\s|_|-)+"," ",
    sub(r"[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+",
    lambda mo: ' ' + mo.group(0).lower(), s)).split())
```

```python
kebab('camelCase') # 'camel-case'
kebab('some text') # 'some-text'
kebab('some-mixed_string With spaces_underscores-and-hyphens')
# 'some-mixed-string-with-spaces-underscores-and-hyphens'
kebab('AllThe-small Things') # 'all-the-small-things'
```
