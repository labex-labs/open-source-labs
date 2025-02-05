# Global Variables

Functions can freely access the values of globals defined in the same file.

```python
name = 'Dave'

def greeting():
    print('Hello', name)  # Using `name` global variable
```

However, functions can't modify globals:

```python
name = 'Dave'

def spam():
  name = 'Guido'

spam()
print(name) # prints 'Dave'
```

**Remember: All assignments in functions are local.**
