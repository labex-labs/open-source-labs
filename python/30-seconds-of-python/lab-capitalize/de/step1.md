# String in Großbuchstaben umwandeln

Schreiben Sie eine Python-Funktion namens `capitalize_string(s, lower_rest=False)`, die einen String als Argument nimmt und einen neuen String zurückgibt, bei dem der erste Buchstabe in Großbuchstaben umgewandelt ist. Die Funktion sollte einen optionalen Parameter `lower_rest` haben, der, wenn er auf `True` gesetzt ist, den Rest des Strings in Kleinbuchstaben umwandelt.

```python
def capitalize(s, lower_rest = False):
  return ''.join([s[:1].upper(), (s[1:].lower() if lower_rest else s[1:])])
```

```python
capitalize('fooBar') # 'FooBar'
capitalize('fooBar', True) # 'Foobar'
```
