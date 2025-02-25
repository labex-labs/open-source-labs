# Verzögerte Funktionsausführung

Schreiben Sie eine Funktion `delay(fn, ms, *args)`, die eine Funktion `fn`, eine Zeit in Millisekunden `ms` und beliebig viele Argumente `args` akzeptiert. Die Funktion sollte die Ausführung von `fn` um `ms` Millisekunden verzögern und sie dann mit den bereitgestellten Argumenten aufrufen. Die Funktion sollte das Ergebnis der Ausführung von `fn` zurückgeben.

Um die Ausführung von `fn` zu verzögern, verwenden Sie die Funktion `time.sleep()`. Diese Funktion nimmt eine Anzahl von Sekunden als Argument entgegen, sodass Sie `ms` in Sekunden umwandeln müssen, bevor Sie sie an `time.sleep()` übergeben.

```python
from time import sleep

def delay(fn, ms, *args):
  sleep(ms / 1000)
  return fn(*args)
```

```python
delay(lambda x: print(x), 1000, 'later') # gibt 'later' nach einer Sekunde aus
```
