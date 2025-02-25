# Fibonacci-Herausforderung

## Problemstellung

Schreiben Sie eine Funktion namens `fibonacci(n)`, die eine ganze Zahl `n` als Parameter nimmt und eine Liste zurückgibt, die die Fibonacci-Folge bis zum n-ten Glied enthält.

Um dieses Problem zu lösen, können Sie die folgenden Schritte ausführen:

1. Erstellen Sie eine leere Liste namens `sequence`.
2. Wenn `n` kleiner oder gleich 0 ist, fügen Sie 0 zur Liste `sequence` hinzu und geben Sie die Liste zurück.
3. Fügen Sie 0 und 1 zur Liste `sequence` hinzu.
4. Verwenden Sie eine `while-Schleife`, um die Summe der letzten beiden Zahlen der Liste `sequence` ans Ende der Liste hinzuzufügen, bis die Länge der Liste `n` erreicht.
5. Geben Sie die Liste `sequence` zurück.

## Beispiel

```python
fibonacci(7) # [0, 1, 1, 2, 3, 5, 8, 13]
```
