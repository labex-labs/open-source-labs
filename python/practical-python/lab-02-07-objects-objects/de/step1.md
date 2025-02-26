# Zuweisung

Viele Operationen in Python beziehen sich auf das _Zuweisen_ oder _Speichern_ von Werten.

```python
a = value         # Zuweisung an eine Variable
s[n] = value      # Zuweisung an eine Liste
s.append(value)   # Anhängen an eine Liste
d['key'] = value  # Hinzufügen zu einem Wörterbuch
```

_Achtung: Zuweisungsoperationen **machen niemals eine Kopie** des zugewiesenen Werts._ Alle Zuweisungen sind lediglich Referenzkopien (oder Zeigerkopien, wenn Sie das bevorzugen).
