# continue-Anweisung

Um ein Element zu überspringen und zum nächsten zu gelangen, verwenden Sie die `continue`-Anweisung.

```python
for line in lines:
    if line == '\n':    # Überspringe leere Zeilen
        continue
    # Weitere Anweisungen
 ...
```

Dies ist nützlich, wenn das aktuelle Element nicht von Interesse ist oder bei der Verarbeitung ignoriert werden muss.
