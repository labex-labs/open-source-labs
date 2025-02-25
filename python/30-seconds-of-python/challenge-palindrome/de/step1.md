# Palindrom

## Problem

Schreiben Sie eine Funktion `palindrome(s)`, die einen String `s` als einzigen Parameter nimmt und `True` zurückgibt, wenn `s` ein Palindrom ist, und `False` sonst. Ihre Funktion sollte bei der Prüfung auf Palindrome die Groß-/Kleinschreibung und nicht-alphanumerische Zeichen ignorieren.

Um dieses Problem zu lösen, können Sie die folgenden Schritte ausführen:

1. Verwenden Sie `str.lower()`, um den String in Kleinbuchstaben umzuwandeln.
2. Verwenden Sie `re.sub()`, um alle nicht-alphanumerischen Zeichen aus dem String zu entfernen.
3. Vergleichen Sie den resultierenden String mit seiner Umkehrung mithilfe der Slicenotation.

## Beispiel

```python
palindrome('taco cat') # True
palindrome('A man, a plan, a canal: Panama') # True
palindrome('hello world') # False
```
