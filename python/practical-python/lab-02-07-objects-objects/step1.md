# Assignment

Many operations in Python are related to _assigning_ or _storing_ values.

```python
a = value         # Assignment to a variable
s[n] = value      # Assignment to a list
s.append(value)   # Appending to a list
d['key'] = value  # Adding to a dictionary
```

_A caution: assignment operations **never make a copy** of the value being assigned._
All assignments are merely reference copies (or pointer copies if you prefer).
