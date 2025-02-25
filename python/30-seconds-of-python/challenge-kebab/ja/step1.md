# ケバブケースの文字列

## 問題

文字列 `s` を入力として受け取り、その文字列のケバブケースバージョンを返す Python 関数 `to_kebab_case(s)` を書きましょう。この関数は次の手順を実行する必要があります。

1. 正規表現 `r"(_|-)+"` を使用して、`-` または `_` をすべてスペースに置き換えます。
2. 文字列内のすべての単語を一致させ、`str.lower()` を使って小文字に変換します。
3. すべての単語を `-` を区切り文字として結合します。

## 例

```python
to_kebab_case('camelCase') # 'camel-case'
to_kebab_case('some text') # 'some-text'
to_kebab_case('some-mixed_string With spaces_underscores-and-hyphens')
# 'some-mixed-string-with-spaces-underscores-and-hyphens'
to_kebab_case('AllThe-small Things') # 'all-the-small-things'
```
