# String to Words Challenge

## Problem
Write a function `string_to_words(s: str, pattern: str = '[a-zA-Z-]+') -> List[str]` that takes a string `s` and an optional `pattern` string as arguments and returns a list of words in the string.

- The function should use `re.findall()` with the supplied `pattern` to find all matching substrings.
- If the `pattern` argument is not provided, the function should use the default regexp, which matches alphanumeric and hyphens.

## Example
```python
string_to_words('I love Python!!') # ['I', 'love', 'Python']
string_to_words('python, javaScript & coffee') # ['python', 'javaScript', 'coffee']
string_to_words('build -q --out one-item', r'\b[a-zA-Z-]+\b') # ['build', 'q', 'out', 'one-item']
```

