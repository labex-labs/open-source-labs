# Verzögerte Funktionsausführung

## Problemstellung

Schreiben Sie eine Funktion `delay(fn, ms, *args)`, die eine Funktion `fn`, eine Zeit in Millisekunden `ms` und beliebig viele Argumente `args` akzeptiert. Die Funktion sollte die Ausführung von `fn` um `ms` Millisekunden verzögern und sie dann mit den bereitgestellten Argumenten aufrufen. Die Funktion sollte das Ergebnis der Ausführung von `fn` zurückgeben.

Um die Ausführung von `fn` zu verzögern, verwenden Sie die Funktion `time.sleep()`. Diese Funktion nimmt eine Anzahl von Sekunden als Argument entgegen, sodass Sie `ms` in Sekunden umwandeln müssen, bevor Sie sie an `time.sleep()` übergeben.

## Beispiel

```python
def add(x, y):
  return x + y

result = delay(add, 2000, 2, 3)
print(result) # Ausgabe: 5
```

Im obigen Beispiel wird die `add`-Funktion um 2000 Millisekunden (2 Sekunden) verzögert, bevor sie mit den Argumenten `2` und `3` aufgerufen wird. Das Ergebnis der `add`-Funktion wird dann zurückgegeben und in der Konsole ausgegeben.
