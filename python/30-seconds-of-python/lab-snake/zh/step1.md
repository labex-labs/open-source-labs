# 蛇形命名法字符串

编写一个名为 `snake` 的Python函数，该函数接受一个字符串作为参数，并返回蛇形命名法格式的字符串。该函数应执行以下步骤：

1. 使用 `re.sub()` 匹配字符串中的所有单词，并用 `str.lower()` 将它们转换为小写。
2. 使用 `re.sub()` 将所有 `-` 字符替换为空格。
3. 最后，使用 `str.join()` 以 `_` 作为分隔符来组合所有单词。

你的函数应该能够处理包含大写和小写字母、空格、连字符和下划线的字符串。

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
