# Inline-Tests

Assertionen können auch für einfache Tests verwendet werden.

```python
def add(x, y):
    return x + y

assert add(2,2) == 4
```

Auf diese Weise integrieren Sie den Test in das gleiche Modul wie Ihren Code.

_Vorteil: Wenn der Code offensichtlich defekt ist, wird das Versuch, das Modul zu importieren, fehlschlagen._

Dies wird nicht für erschöpfende Tests empfohlen. Es ist eher ein grundlegender "Smoke-Test". Funktioniert die Funktion überhaupt mit einem Beispiel? Wenn nicht, dann ist definitiv etwas kaputt.
