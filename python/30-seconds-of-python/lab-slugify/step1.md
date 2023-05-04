# String to Slug Challenge

Write a function `slugify(s)` that takes a string `s` as an argument and returns a slug. The function should perform the following operations:

1. Convert the string to lowercase and remove any leading or trailing whitespace.
2. Replace all special characters (i.e., any character that is not a letter, digit, whitespace, hyphen, or underscore) with an empty string.
3. Replace all whitespace, hyphens, and underscores with a single hyphen.
4. Remove any leading or trailing hyphens.

```py
import re

def slugify(s):
  s = s.lower().strip()
  s = re.sub(r'[^\w\s-]', '', s)
  s = re.sub(r'[\s_-]+', '-', s)
  s = re.sub(r'^-+|-+$', '', s)
  return s
```

```py
slugify('Hello World!') # 'hello-world'
```
