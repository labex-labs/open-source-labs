# Den ersten Buchstaben einer Zeichenkette in Kleinbuchstaben umwandeln

## Problemstellung

Schreiben Sie eine Funktion `decapitalize(s, upper_rest = False)`, die eine Zeichenkette `s` annimmt und eine neue Zeichenkette zurückgibt, bei der der erste Buchstabe in Kleinbuchstaben umgewandelt ist. Die Funktion sollte auch einen optionalen Parameter `upper_rest` haben, der, wenn er auf `True` gesetzt ist, den Rest der Zeichenkette in Großbuchstaben umwandeln wird.

## Beispiel

```python
decapitalize('FooBar') # 'fooBar'
decapitalize('FooBar', True) # 'fOOBAR'
```
