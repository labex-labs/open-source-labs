# 文字列からスラッグへのチャレンジ

## 問題

文字列 `s` を引数として受け取り、スラッグを返す関数 `slugify(s)` を書きなさい。この関数は次の操作を行う必要があります。

1. 文字列を小文字に変換し、先頭または末尾の空白を削除する。
2. すべての特殊文字（つまり、文字、数字、空白、ハイフン、またはアンダースコアでない任意の文字）を空文字列に置き換える。
3. すべての空白、ハイフン、およびアンダースコアを単一のハイフンに置き換える。
4. 先頭または末尾のハイフンを削除する。

## 例

```python
slugify('Hello World!') # 'hello-world'
slugify('  My Example 123  ') # 'my-example-123'
slugify('This is a long sentence with spaces and punctuation!') # 'this-is-a-long-sentence-with-spaces-and-punctuation'
```
