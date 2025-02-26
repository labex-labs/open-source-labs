# Wachstum von Listen

Python-Listen sind hoch optimiert für das Ausführen von `append()`-Operationen. Jedes Mal, wenn eine Liste wächst, greift sie einen größeren Arbeitsspeicherbereich als tatsächlich erforderlich, mit der Erwartung, dass später weitere Daten zur Liste hinzugefügt werden. Wenn neue Elemente hinzugefügt werden und Speicherplatz verfügbar ist, speichert die `append()`-Operation das Element ohne weitere Arbeitsspeicherzuweisung.

Experimentieren Sie mit dieser Eigenschaft von Listen, indem Sie die `sys.getsizeof()`-Funktion auf einer Liste anwenden und einige weitere Elemente anhängen.

```python
>>> import sys
>>> items = []
>>> sys.getsizeof(items)
64
>>> items.append(1)
>>> sys.getsizeof(items)
96
>>> items.append(2)
>>> sys.getsizeof(items)    # Beachten Sie, wie die Größe nicht zunimmt
96
>>> items.append(3)
>>> sys.getsizeof(items)    # Hier erhöht sich die Größe immer noch nicht
96
>>> items.append(4)
>>> sys.getsizeof(items)    # Noch nicht.
96
>>> items.append(5)
>>> sys.getsizeof(items)    # Beachten Sie, dass die Größe sprunghaft angestiegen ist
128
>>>
```

Eine Liste speichert ihre Elemente per Referenz. Daher ist der für jedes Element erforderliche Arbeitsspeicher eine einzelne Speicheradresse. Auf einem 64-Bit-Rechner ist eine Adresse typischerweise 8 Byte. Wenn Python jedoch für 32 Bit kompiliert wurde, kann es 4 Byte sein, und die Zahlen für das obige Beispiel werden die Hälfte der angezeigten Zahlen sein.
