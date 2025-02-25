# String-Anagram-Herausforderung

## Problem

Schreiben Sie eine Funktion `is_anagram(s1, s2)`, die zwei Zeichenketten als Argumente nimmt und `True` zurückgibt, wenn sie einander Anagramme sind, und `False` sonst. Die Funktion sollte grob- und kleinschreibungseinvariant sein und Leerzeichen, Satzzeichen und Sonderzeichen ignorieren.

Um dieses Problem zu lösen, können Sie die folgenden Schritte ausführen:

1. Verwenden Sie `str.isalnum()`, um nicht-alphanumerische Zeichen zu filtern, und `str.lower()`, um jedes Zeichen in Kleinbuchstaben umzuwandeln.
2. Verwenden Sie `collections.Counter`, um die resultierenden Zeichen für jede Zeichenkette zu zählen und die Ergebnisse zu vergleichen.

## Beispiel

```python
is_anagram('#anagram', 'Nag a ram!')  # True
is_anagram('hello', 'world')  # False
```
