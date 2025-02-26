# Defekte reload()

Erstellen Sie eine Instanz:

```python
>>> import simplemod
>>> s = simplemod.Spam()
>>> s.yow()
Yow!
>>>
```

Gehen Sie nun zur Datei `simplemod.py` und ändern Sie die Implementierung von `Spam.yow()` wie folgt:

```python
# simplemod.py
...

class Spam:
    def yow(self):
        print('More Yow!')
```

Beobachten Sie nun, was passiert, wenn Sie das Modul neu laden. Starten Sie für diesen Teil nicht Python neu.

```python
>>> importlib.reload(simplemod)
simplemod geladen
<module'simplemod' from'simplemod.py'>
>>> s.yow()
'Yow!'
>>> t = simplemod.Spam()
>>> t.yow()
'More Yow!'
>>>
```

Beobachten Sie, wie Sie zwei Instanzen von `Spam` haben, aber sie unterschiedliche Implementierungen der `yow()`-Methode verwenden. Ja, tatsächlich werden beide Codeversionen gleichzeitig geladen. Sie werden auch andere Merkwürdigkeiten finden. Beispielsweise:

```python
>>> s
<simplemod.Spam Objekt am 0x1006940b8>
>>> isinstance(s, simplemod.Spam)
False
>>> isinstance(t, simplemod.Spam)
True
>>>
```

Zusammenfassung: Es ist wahrscheinlich am besten, sich nicht auf das Neuladen für etwas Wichtiges zu verlassen. Es kann in Ordnung sein, wenn Sie nur etwas debuggen möchten (solange Sie sich dessen Einschränkungen und Gefahren bewusst sind).
