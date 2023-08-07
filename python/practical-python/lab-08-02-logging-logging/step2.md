# Exceptions Revisited

In the exercises, we wrote a function `parse()` that looked something like this:

```python
# fileparse.py
def parse(f, types=None, names=None, delimiter=None):
    records = []
    for line in f:
        line = line.strip()
        if not line: continue
        try:
            records.append(split(line,types,names,delimiter))
        except ValueError as e:
            print("Couldn't parse :", line)
            print("Reason :", e)
    return records
```

Focus on the `try-except` statement. What should you do in the `except` block?

Should you print a warning message?

```python
try:
    records.append(split(line,types,names,delimiter))
except ValueError as e:
    print("Couldn't parse :", line)
    print("Reason :", e)
```

Or do you silently ignore it?

```python
try:
    records.append(split(line,types,names,delimiter))
except ValueError as e:
    pass
```

Neither solution is satisfactory because you often want _both_ behaviors (user selectable).
