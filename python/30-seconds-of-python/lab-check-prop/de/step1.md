# Überprüfe Eigenschaft

Erstelle eine Funktion namens `check_prop`, die zwei Parameter annimmt: `fn` und `prop`. Der Parameter `fn` ist eine Prädikatsfunktion, die auf die angegebene Eigenschaft eines Wörterbuchs angewendet werden wird. Der Parameter `prop` ist ein String, der den Namen der Eigenschaft darstellt, auf die die Prädikatsfunktion angewendet werden wird.

Die Funktion `check_prop` sollte eine Lambda-Funktion zurückgeben, die ein Wörterbuch annimmt und die Prädikatsfunktion `fn` auf die angegebene Eigenschaft anwendet.

```python
def check_prop(fn, prop):
  return lambda obj: fn(obj[prop])
```

```python
check_age = check_prop(lambda x: x >= 18, 'age')
user = {'name': 'Mark', 'age': 18}
check_age(user) # True
```
