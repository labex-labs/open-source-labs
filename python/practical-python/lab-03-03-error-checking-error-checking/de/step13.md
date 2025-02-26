# `with`-Anweisung

In modernem Code wird `try-finally` oft durch die `with`-Anweisung ersetzt.

```python
lock = Lock()
with lock:
    # lock acquired
  ...
# lock released
```

Ein vertrauteres Beispiel:

```python
with open(filename) as f:
    # Verwenden Sie die Datei
  ...
# Datei geschlossen
```

`with` definiert einen Verwendungskontext für eine Ressource. Wenn die Ausführung diesen Kontext verlässt, werden die Ressourcen freigegeben. `with` funktioniert nur mit bestimmten Objekten, die speziell programmiert wurden, um dies zu unterstützen.
