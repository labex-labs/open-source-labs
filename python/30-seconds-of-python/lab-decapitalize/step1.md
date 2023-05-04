# Decapitalize String

Write a function `decapitalize(s, upper_rest = False)` that takes a string `s` and returns a new string with the first letter decapitalized. The function should also have an optional parameter `upper_rest` that, when set to `True`, will convert the rest of the string to uppercase.

```py
def decapitalize(s, upper_rest = False):
  return ''.join([s[:1].lower(), (s[1:].upper() if upper_rest else s[1:])])
```

```py
decapitalize('FooBar') # 'fooBar'
decapitalize('FooBar', True) # 'fOOBAR'
```
