# `import as` statement

You can change the name of a module as you import it:

```python
import math as m
def rectangular(r, theta):
    x = r * m.cos(theta)
    y = r * m.sin(theta)
    return x, y
```

It works the same as a normal import. It just renames the module in that one file.
