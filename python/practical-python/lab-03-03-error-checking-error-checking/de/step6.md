# Das Fangen von mehreren Fehlern

Sie können verschiedene Arten von Ausnahmen mit mehreren `except`-Blöcken fangen.

```python
try:
...
except LookupError as e:
...
except RuntimeError as e:
...
except IOError as e:
...
except KeyboardInterrupt as e:
...
```

Alternativ können Sie sie gruppieren, wenn die Anweisungen, um sie zu behandeln, dieselben sind:

```python
try:
...
except (IOError,LookupError,RuntimeError) as e:
...
```
