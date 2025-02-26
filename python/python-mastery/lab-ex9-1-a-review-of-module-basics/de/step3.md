# Wiederholte Modulladung

Stellen Sie sicher, dass Sie verstehen, dass Module nur einmal geladen werden. Versuchen Sie eine wiederholte Importierung und beobachten Sie, wie Sie die Ausgabe der `print`-Funktion nicht sehen:

```python
>>> import simplemod
>>>
```

Versuchen Sie, den Wert von `x` zu ändern und sehen Sie, dass eine wiederholte Importierung keinen Effekt hat.

```python
>>> simplemod.x
42
>>> simplemod.x = 13
>>> simplemod.x
13
>>> import simplemod
>>> simplemod.x
13
>>>
```

Verwenden Sie `importlib.reload()`, wenn Sie ein Modul erneut laden möchten.

```python
>>> import importlib
>>> importlib.reload(simplemod)
simplemod geladen
<module'simplemod' from'simplemod.py'>
>>> simplemod.x
42
>>>
```

`sys.modules` ist ein Wörterbuch aller geladenen Module. Schauen Sie sich es an, löschen Sie Ihr Modul und versuchen Sie eine wiederholte Importierung.

```python
>>> sys.modules
... schauen Sie sich die Ausgabe an...
>>> sys.modules['simplemod']
<module'simplemod' from'simplemod.py'>
>>> del sys.modules['simplemod']
>>> import simplemod
simplemod geladen
>>>
```
