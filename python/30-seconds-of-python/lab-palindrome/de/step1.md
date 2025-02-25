# Palindrom

Schreiben Sie eine Funktion `palindrome(s)`, die einen String `s` als einzigen Parameter nimmt und `True` zurückgibt, wenn `s` ein Palindrom ist, und `False` sonst. Ihre Funktion sollte die Groß-/Kleinschreibung und nicht-alphanumerische Zeichen beim Überprüfen auf Palindrome ignorieren.

Um dieses Problem zu lösen, können Sie die folgenden Schritte ausführen:

1. Verwenden Sie `str.lower()`, um den String in Kleinbuchstaben umzuwandeln.
2. Verwenden Sie `re.sub()`, um alle nicht-alphanumerischen Zeichen aus dem String zu entfernen.
3. Vergleichen Sie den resultierenden String mit seiner Umkehrung mithilfe der Slicenotation.

```python
from re import sub

def palindrome(s):
  s = sub('[\W_]', '', s.lower())
  return s == s[::-1]
```

```python
palindrome('taco cat') # True
```
