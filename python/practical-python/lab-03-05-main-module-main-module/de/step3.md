# `__main__`-Prüfung

Es ist üblich, dass Module, die als Hauptskript ausgeführt werden, diese Konvention verwenden:

```python
# prog.py
...
if __name__ == '__main__':
    # Wird als Hauptprogramm ausgeführt...
    Anweisungen
  ...
```

Die Anweisungen, die innerhalb der `if`-Anweisung eingeschlossen sind, werden zum `main`-Programm.
