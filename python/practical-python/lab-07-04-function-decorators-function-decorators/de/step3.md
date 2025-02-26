# Code, der Logging durchführt

Vielleicht können Sie eine Funktion schreiben, die Funktionen mit hinzugefügtem Logging erstellt. Ein Wrapper.

```python
def logged(func):
    def wrapper(*args, **kwargs):
        print('Calling', func.__name__)
        return func(*args, **kwargs)
    return wrapper
```

Nun verwenden Sie es.

```python
def add(x, y):
    return x + y

logged_add = logged(add)
```

Was passiert, wenn Sie die von `logged` zurückgegebene Funktion aufrufen?

```python
logged_add(3, 4)      # Sie sehen die Log-Nachricht erscheinen
```

Dieses Beispiel veranschaulicht den Prozess des Erstellens einer sogenannten _Wrapper-Funktion_.

Ein Wrapper ist eine Funktion, die um eine andere Funktion herumgeht und einige zusätzliche Verarbeitungsbits hat, aber sonst genauso funktioniert wie die ursprüngliche Funktion.

```python
>>> logged_add(3, 4)
Calling add   # Zusätzliche Ausgabe. Hinzugefügt durch den Wrapper
7
>>>
```

_Hinweis: Die `logged()`-Funktion erstellt den Wrapper und gibt ihn als Ergebnis zurück._
