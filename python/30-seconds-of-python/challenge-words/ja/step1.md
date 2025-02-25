# 文字列から単語へのチャレンジ

## 問題

文字列`s`とオプションの`pattern`文字列を引数として受け取り、文字列内の単語のリストを返す関数`string_to_words(s: str, pattern: str = '[a-zA-Z-]+') -> List[str]`を書きます。

- 関数は、提供された`pattern`を使用して`re.findall()`を使って、すべての一致する部分文字列を見つける必要があります。
- `pattern`引数が提供されない場合、関数は既定の正規表現を使用して、英数字とハイフンに一致する必要があります。

## 例

```python
string_to_words('I love Python!!') # ['I', 'love', 'Python']
string_to_words('python, javaScript & coffee') # ['python', 'javaScript', 'coffee']
string_to_words('build -q --out one-item', r'\b[a-zA-Z-]+\b') # ['build', 'q', 'out', 'one-item']
```
