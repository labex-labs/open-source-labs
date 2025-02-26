# Veränderbare Ganzzahlen

Python-Ganzzahlen sind normalerweise unveränderbar. Angenommen, du wolltest jedoch ein veränderbares Ganzzahl-Objekt erstellen. Beginne damit, eine Klasse wie diese zu definieren:

```python
# mutint.py

class MutInt:
    __slots__ = ['value']

    def __init__(self, value):
        self.value = value
```

Teste es:

```python
>>> a = MutInt(3)
>>> a
<__main__.MutInt Objekt am 0x10e79d408>
>>> a.value
3
>>> a.value = 42
>>> a.value
42
>>> a + 10
Fehler (letzte Aufrufzeile):
  Datei "<stdin>", Zeile 1, in <modul>
TypeError: nicht unterstützte Operandentypen für +: 'MutInt' und 'int'
>>>
```

Alles sehr aufregend, nur dass mit diesem neuen `MutInt`-Objekt eigentlich nichts funktioniert. Das Drucken ist schrecklich, keine der mathematischen Operatoren funktioniert und es ist im Grunde ziemlich nutzlos. Nichtsdestotrotz ist dessen Wert veränderbar - das hat es zumindest.
