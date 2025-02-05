# Catching Multiple Errors

You can catch different kinds of exceptions using multiple `except` blocks.

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

Alternatively, if the statements to handle them is the same, you can group them:

```python
try:
  ...
except (IOError,LookupError,RuntimeError) as e:
  ...
```
