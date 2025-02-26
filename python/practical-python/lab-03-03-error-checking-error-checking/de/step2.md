# Ausnahmen

Ausnahmen werden verwendet, um Fehler zu signalisieren. Um selbst eine Ausnahme zu erhöhen, verwenden Sie die `raise`-Anweisung.

```python
if name not in authorized:
    raise RuntimeError(f'{name} not authorized')
```

Um eine Ausnahme zu fangen, verwenden Sie `try-except`.

```python
try:
    authenticate(username)
except RuntimeError as e:
    print(e)
```
