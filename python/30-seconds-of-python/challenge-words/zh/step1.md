# 字符串转单词挑战

## 问题

编写一个函数 `string_to_words(s: str, pattern: str = '[a-zA-Z-]+') -> List[str]`，该函数接受一个字符串 `s` 和一个可选的 `pattern` 字符串作为参数，并返回字符串中的单词列表。

- 该函数应使用 `re.findall()` 和提供的 `pattern` 来查找所有匹配的子字符串。
- 如果未提供 `pattern` 参数，该函数应使用默认的正则表达式，该表达式匹配字母数字和连字符。

## 示例

```python
string_to_words('I love Python!!') # ['I', 'love', 'Python']
string_to_words('python, javaScript & coffee') # ['python', 'javaScript', 'coffee']
string_to_words('build -q --out one-item', r'\b[a-zA-Z-]+\b') # ['build', 'q', 'out', 'one-item']
```
