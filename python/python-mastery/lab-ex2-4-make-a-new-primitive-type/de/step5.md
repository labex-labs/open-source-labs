# Konvertierungen

Dein neues primitiver Datentyp ist fast fertig. Du möchtest ihm möglicherweise die Fähigkeit geben, mit einigen üblichen Konvertierungen umzugehen. Beispielsweise:

```python
>>> a = MutInt(3)
>>> int(a)
Fehler (letzte Aufrufzeile):
  Datei "<stdin>", Zeile 1, in <modul>
TypeError: int() Argument muss ein String, ein bytes-ähnliches Objekt oder eine Zahl sein, nicht 'MutInt'
>>> float(a)
Fehler (letzte Aufrufzeile):
  Datei "<stdin>", Zeile 1, in <modul>
TypeError: float() Argument muss ein String, ein bytes-ähnliches Objekt oder eine Zahl sein, nicht 'MutInt'
>>>
```

Du kannst deiner Klasse eine `__int__()`- und `__float__()`-Methode geben, um dies zu beheben:

```python
from functools import total_ordering

@total_ordering
class MutInt:
    __slots__ = ['value']

    def __init__(self, value):
        self.value = value

 ...

    def __int__(self):
        return self.value

    def __float__(self):
        return float(self.value)
```

Jetzt kannst du richtig konvertieren:

```python
>>> a = MutInt(3)
>>> int(a)
3
>>> float(a)
3.0
>>>
```

Allgemein gilt jedoch, dass Python Daten niemals automatisch konvertiert. Also, auch wenn du der Klasse eine `__int__()`-Methode gegeben hast, wird `MutInt` in allen Situationen, in denen möglicherweise eine Ganzzahl erwartet wird, immer noch nicht funktionieren. Beispielsweise beim Indexieren:

```python
>>> names = ['Dave', 'Guido', 'Paula', 'Thomas', 'Lewis']
>>> a = MutInt(1)
>>> names[a]
Fehler (letzte Aufrufzeile):
  Datei "<stdin>", Zeile 1, in <modul>
TypeError: Listenindizes müssen Ganzzahlen oder Slices sein, nicht MutInt
>>>
```

Dies kann behoben werden, indem du `MutInt` eine `__index__()`-Methode gibst, die eine Ganzzahl liefert. Ändere die Klasse wie folgt:

```python
from functools import total_ordering

@total_ordering
class MutInt:
    __slots__ = ['value']

    def __init__(self, value):
        self.value = value

 ...

    def __int__(self):
        return self.value

    __index__ = __int__     # Ermöglicht das Indexieren
```

**Diskussion**

Das Erstellen eines neuen primitiven Datentyps ist tatsächlich eine der kompliziertesten Programmieraufgaben in Python. Es gibt viele Randfälle und niedrigere Ebene-Probleme, über die man sich Sorgen machen muss - insbesondere was die Interaktion deines Typs mit anderen Python-Typen betrifft. Wahrscheinlich das Wichtigste, das man im Kopf behalten sollte, ist, dass du fast jeden Aspekt der Interaktion eines Objekts mit dem Rest von Python anpassen kannst, wenn du die zugrunde liegenden Protokolle kennst. Wenn du das machen möchtest, ist es ratsam, den vorhandenen Code nach etwas Ähnlichem zu deinem Versuch zu durchsuchen.
