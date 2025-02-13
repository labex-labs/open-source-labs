# 短横线命名法字符串

## 问题

编写一个名为 `to_kebab_case(s)` 的 Python 函数，该函数接受一个字符串 `s` 作为输入，并返回该字符串的短横线命名法版本。该函数应执行以下步骤：

1. 使用正则表达式 `r"(_|-)+"` 将任何 `-` 或 `_` 替换为空格。
2. 匹配字符串中的所有单词，使用 `str.lower()` 将它们转换为小写。
3. 使用 `-` 作为分隔符组合所有单词。

## 示例

```python
to_kebab_case('camelCase') # 'camel-case'
to_kebab_case('some text') # 'some-text'
to_kebab_case('some-mixed_string With spaces_underscores-and-hyphens')
# 'some-mixed-string-with-spaces-underscores-and-hyphens'
to_kebab_case('AllThe-small Things') # 'all-the-small-things'
```
