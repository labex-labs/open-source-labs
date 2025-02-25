# 回文

## 問題

文字列`s`を唯一のパラメータとして受け取り、`s`が回文の場合には`True`を返し、それ以外の場合には`False`を返す関数`palindrome(s)`を書きます。回文をチェックする際には、大文字小文字の区別と非アルファベット数字の文字を無視する必要があります。

この問題を解くには、次の手順を辿ることができます。

1. `str.lower()`を使用して文字列を小文字に変換します。
2. `re.sub()`を使用して文字列からすべての非アルファベット数字の文字を削除します。
3. スライス表記を使用して、結果の文字列をその逆と比較します。

## 例

```python
palindrome('taco cat') # True
palindrome('A man, a plan, a canal: Panama') # True
palindrome('hello world') # False
```
