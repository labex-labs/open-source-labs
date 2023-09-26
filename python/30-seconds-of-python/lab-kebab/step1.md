# Kebabcase string

Write a Python function called `to_kebab_case(s)` that takes a string `s` as its input and returns the kebab case version of the string. The function should perform the following steps:

1. Replace any `-` or `_` with a space, using the regexp `r"(_|-)+"`.
2. Match all words in the string, `str.lower()` to lowercase them.
3. Combine all words using `-` as the separator.

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
