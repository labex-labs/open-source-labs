# Capitalize String

Write a Python function called `capitalize_string(s, lower_rest=False)` that takes a string as an argument and returns a new string with the first letter capitalized. The function should have an optional parameter `lower_rest` which, if set to `True`, converts the rest of the string to lowercase.

```py
def capitalize(s, lower_rest = False):
  return ''.join([s[:1].upper(), (s[1:].lower() if lower_rest else s[1:])])
```

```py
capitalize('fooBar') # 'FooBar'
capitalize('fooBar', True) # 'Foobar'
```
