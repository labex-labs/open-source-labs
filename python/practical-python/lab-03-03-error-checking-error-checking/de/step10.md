# Wiedererhöhung einer Ausnahme

Verwenden Sie `raise`, um einen gefangenen Fehler zu propagieren.

```python
try:
    go_do_something()
except Exception as e:
    print('Computer sagt nein. Grund :', e)
    raise
```

Dies ermöglicht es Ihnen, Maßnahmen zu ergreifen (z.B. Protokollierung) und den Fehler an den Aufrufer weiterzugeben.
