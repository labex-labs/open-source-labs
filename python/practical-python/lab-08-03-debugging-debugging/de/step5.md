# Der Python-Debugger

Sie können den Debugger manuell innerhalb eines Programms starten.

```python
def some_function():
  ...
    breakpoint()      # Startet den Debugger (Python 3.7+)
  ...
```

Dies startet den Debugger beim Aufruf von `breakpoint()`.

In früheren Python-Versionen mussten Sie das so machen. Manchmal finden Sie dies in anderen Debugging-Anleitungen erwähnt.

```python
import pdb
...
pdb.set_trace()       # Anstelle von `breakpoint()`
...
```
