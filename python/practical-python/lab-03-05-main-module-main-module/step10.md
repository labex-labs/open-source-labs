# Program Exit

Program exit is handled through exceptions.

```python
raise SystemExit
raise SystemExit(exitcode)
raise SystemExit('Informative message')
```

An alternative.

```python
import sys
sys.exit(exitcode)
```

A non-zero exit code indicates an error.
