# `finally`-Anweisung

Sie gibt an, welche Codezeilen unabhängig davon ausgeführt werden müssen, ob eine Ausnahme auftritt oder nicht.

```python
lock = Lock()
...
lock.acquire()
try:
  ...
finally:
    lock.release()  # Dies wird IMMER ausgeführt. Mit und ohne Ausnahme.
```

Wird häufig verwendet, um Ressourcen sicher zu verwalten (insbesondere Locks, Dateien usw.).
