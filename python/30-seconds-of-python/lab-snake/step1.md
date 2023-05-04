# Snakecase String

Write a Python function called `snake` that takes a string as its argument and returns the string in snake case. The function should perform the following steps:

1. Use `re.sub()` to match all words in the string, `str.lower()` to lowercase them.
2. Use `re.sub()` to replace any `-` characters with spaces.
3. Finally, use `str.join()` to combine all words using `_` as the separator.

Your function should be able to handle strings with a mix of uppercase and lowercase letters, spaces, hyphens, and underscores.

```py
from re import sub

def snake(s):
  return '_'.join(
    sub('([A-Z][a-z]+)', r' \1',
    sub('([A-Z]+)', r' \1',
    s.replace('-', ' '))).split()).lower()
```

```py
snake('camelCase') # 'camel_case'
snake('some text') # 'some_text'
snake('some-mixed_string With spaces_underscores-and-hyphens')
# 'some_mixed_string_with_spaces_underscores_and_hyphens'
snake('AllThe-small Things') # 'all_the_small_things'
```
