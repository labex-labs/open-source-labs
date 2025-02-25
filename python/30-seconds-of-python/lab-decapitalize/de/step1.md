# Den ersten Buchstaben einer Zeichenkette in Kleinbuchstaben umwandeln

Schreiben Sie eine Funktion `decapitalize(s, upper_rest = False)`, die eine Zeichenkette `s` nimmt und eine neue Zeichenkette zurückgibt, bei der der erste Buchstabe in Kleinbuchstaben umgewandelt ist. Die Funktion sollte auch einen optionalen Parameter `upper_rest` haben, der, wenn er auf `True` gesetzt ist, den Rest der Zeichenkette in Großbuchstaben umwandeln wird.

```python
def decapitalize(s, upper_rest = False):
  return ''.join([s[:1].lower(), (s[1:].upper() if upper_rest else s[1:])])
```

```python
decapitalize('FooBar') # 'fooBar'
decapitalize('FooBar', True) # 'fOOBAR'
```
