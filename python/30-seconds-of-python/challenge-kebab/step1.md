# Kebabcase string

## Problem
Write a Python function called `to_kebab_case(s)` that takes a string `s` as its input and returns the kebab case version of the string. The function should perform the following steps:
1. Replace any `-` or `_` with a space, using the regexp `r"(_|-)+"`.
2. Match all words in the string, `str.lower()` to lowercase them.
3. Combine all words using `-` as the separator.

## Example
```py
to_kebab_case('camelCase') # 'camel-case'
to_kebab_case('some text') # 'some-text'
to_kebab_case('some-mixed_string With spaces_underscores-and-hyphens')
# 'some-mixed-string-with-spaces-underscores-and-hyphens'
to_kebab_case('AllThe-small Things') # 'all-the-small-things'
```

