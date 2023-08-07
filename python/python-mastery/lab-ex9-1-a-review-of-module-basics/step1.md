# Preparation

This exercise is about some of the more tricky details of library modules. Start this exercise by creating a very simple library module:

```python
# simplemod.py

x = 42        # A global variable

# A simple function
def foo():
    print('x is', x)

# A simple class
class Spam:
    def yow(self):
        print('Yow!')

# A scripting statement
print('Loaded simplemod')
```
