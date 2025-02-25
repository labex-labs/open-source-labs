# Benutzereigene Funktionen

Verwenden Sie Funktionen für Code, den Sie wiederverwenden möchten. Hier ist eine Funktionsdefinition:

```python
def sumcount(n):
    '''
    Gibt die Summe der ersten n ganzen Zahlen zurück
    '''
    total = 0
    while n > 0:
        total += n
        n -= 1
    return total
```

Um eine Funktion aufzurufen.

```python
a = sumcount(100)
```

Eine Funktion ist eine Reihe von Anweisungen, die eine bestimmte Aufgabe ausführen und ein Ergebnis zurückgeben. Das Schlüsselwort `return` ist erforderlich, um den Rückgabewert der Funktion explizit anzugeben.
