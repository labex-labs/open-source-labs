# String to Words

Write a function `string_to_words(s: str, pattern: str = '[a-zA-Z-]+') -> List[str]` that takes a string `s` and an optional `pattern` string as arguments and returns a list of words in the string.

- The function should use `re.findall()` with the supplied `pattern` to find all matching substrings.
- If the `pattern` argument is not provided, the function should use the default regexp, which matches alphanumeric and hyphens.

```py
import re

def words(s, pattern = '[a-zA-Z-]+'):
  return re.findall(pattern, s)
```

```py
words('I love Python!!') # ['I', 'love', 'Python']
words('python, javaScript & coffee') # ['python', 'javaScript', 'coffee']
words('build -q --out one-item', r'\b[a-zA-Z-]+\b')
# ['build', 'q', 'out', 'one-item']
```
