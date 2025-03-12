# Untersuchung der Stack-Frame-Inspektion

Der von uns verwendete Ansatz `_init(locals())` funktioniert, hat aber einen Nachteil. Jedes Mal, wenn wir eine `__init__`-Methode definieren, müssen wir explizit `locals()` aufrufen. Dies kann etwas umständlich werden, insbesondere wenn es um mehrere Klassen geht. Glücklicherweise können wir unseren Code sauberer und effizienter gestalten, indem wir die Stack-Frame-Inspektion nutzen. Diese Technik ermöglicht es uns, automatisch auf die lokalen Variablen des Aufrufers zuzugreifen, ohne `locals()` explizit aufrufen zu müssen.

Lassen Sie uns diese Technik im Python-Interpreter untersuchen. Zunächst öffnen Sie Ihr Terminal und navigieren Sie in das Projektverzeichnis. Starten Sie dann den Python-Interpreter. Sie können dies tun, indem Sie die folgenden Befehle ausführen:

```bash
cd ~/project
python3
```

Jetzt, da wir im Python-Interpreter sind, müssen wir das `sys`-Modul importieren. Das `sys`-Modul bietet Zugang zu einigen Variablen, die vom Python-Interpreter verwendet oder verwaltet werden. Wir werden es nutzen, um auf die Stack-Frame-Informationen zuzugreifen.

```python
import sys
```

Als Nächstes definieren wir eine verbesserte Version unserer `_init()`-Funktion. Diese neue Version wird direkt auf den Frame des Aufrufers zugreifen, sodass es nicht mehr erforderlich ist, `locals()` explizit zu übergeben.

```python
def _init():
    # Get the caller's frame (1 level up in the call stack)
    frame = sys._getframe(1)

    # Get the local variables from that frame
    locs = frame.f_locals

    # Extract self and set other variables as attributes
    self = locs.pop('self')
    for name, val in locs.items():
        setattr(self, name, val)
```

In diesem Code ruft `sys._getframe(1)` das Frame-Objekt der aufrufenden Funktion ab. Das Argument `1` bedeutet, dass wir eine Ebene höher im Aufrufstack suchen. Sobald wir das Frame-Objekt haben, können wir seine lokalen Variablen über `frame.f_locals` zugreifen. Dies gibt uns ein Wörterbuch aller lokalen Variablen im Geltungsbereich des Aufrufers. Wir extrahieren dann die `self`-Variable und setzen die verbleibenden Variablen als Attribute des `self`-Objekts.

Jetzt testen wir diese neue `_init()`-Funktion mit einer neuen Version unserer `Stock`-Klasse.

```python
class Stock:
    def __init__(self, name, shares, price):
        _init()  # No need to pass locals() anymore!

# Test it
s = Stock('GOOG', 100, 490.1)
print(s.name, s.shares, s.price)

# Also works with keyword arguments
s = Stock(name='AAPL', shares=50, price=125.3)
print(s.name, s.shares, s.price)
```

Wie Sie sehen können, muss die `__init__`-Methode nicht mehr explizit `locals()` übergeben. Dies macht unseren Code sauberer und leichter lesbar aus Sicht des Aufrufers.

### Wie die Stack-Frame-Inspektion funktioniert

Wenn Sie `sys._getframe(1)` aufrufen, gibt Python das Frame-Objekt zurück, das den Ausführungsframe des Aufrufers repräsentiert. Das Argument `1` bedeutet "eine Ebene über dem aktuellen Frame" (der aufrufenden Funktion).

Ein Frame-Objekt enthält wichtige Informationen über den Ausführungskontext. Dies umfasst die aktuell ausgeführte Funktion, die lokalen Variablen in dieser Funktion und die aktuell ausgeführte Zeilennummer.

Durch den Zugriff auf `frame.f_locals` erhalten wir ein Wörterbuch aller lokalen Variablen im Geltungsbereich des Aufrufers. Dies ist ähnlich wie das, was `locals()` zurückgeben würde, wenn es direkt aus diesem Geltungsbereich aufgerufen würde.

Diese Technik ist recht leistungsstark, sollte aber mit Vorsicht angewendet werden. Sie wird im Allgemeinen als fortgeschrittenes Python-Feature angesehen und kann etwas "magisch" erscheinen, da sie über die normalen Geltungsbereichsgrenzen von Python hinausgreift.

Sobald Sie mit der Untersuchung der Stack-Frame-Inspektion fertig sind, können Sie den Python-Interpreter beenden, indem Sie den folgenden Befehl ausführen:

```python
exit()
```
