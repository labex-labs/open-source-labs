# Reassigning values

Reassigning a value _never_ overwrites the memory used by the previous value.

```python
a = [1,2,3]
b = a
a = [4,5,6]

print(a)      # [4, 5, 6]
print(b)      # [1, 2, 3]    Holds the original value
```

Remember: **Variables are names, not memory locations.**
