# Eigenschaft überprüfen

## Problem

Erstellen Sie eine Funktion namens `check_prop`, die zwei Parameter annimmt: `fn` und `prop`. Der `fn`-Parameter ist eine Prädikatsfunktion, die auf die angegebene Eigenschaft eines Dictionaries angewendet wird. Der `prop`-Parameter ist ein String, der den Namen der Eigenschaft darstellt, auf die die Prädikatsfunktion angewendet wird.

Die `check_prop`-Funktion sollte eine Lambda-Funktion zurückgeben, die ein Dictionary annimmt und die Prädikatsfunktion `fn` auf die angegebene Eigenschaft anwendet.

## Beispiel

```python
check_age = check_prop(lambda x: x >= 18, 'age')
user = {'name': 'Mark', 'age': 18}
check_age(user) # True
```

Im obigen Beispiel erstellen wir eine `check_age`-Funktion, die überprüft, ob der Wert der `age`-Eigenschaft in einem Dictionary größer oder gleich 18 ist. Anschließend erstellen wir ein `user`-Dictionary mit einem Namen und einer age-Eigenschaft. Schließlich rufen wir die `check_age`-Funktion mit dem `user`-Dictionary als Argument auf, was `True` zurückgibt, da die age-Eigenschaft gleich 18 ist.
