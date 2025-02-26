# Das Fangen aller Fehler

Um jede Ausnahme zu fangen, verwenden Sie `Exception` wie folgt:

```python
try:
...
except Exception:       # GEFÄHR. Siehe unten
    print('An error occurred')
```

Im Allgemeinen ist es ein schlechter Gedanke, so etwas zu schreiben, da Sie nicht wissen, warum es fehlgeschlagen ist.
