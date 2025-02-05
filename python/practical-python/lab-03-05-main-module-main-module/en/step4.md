# Main programs vs. library imports

Any Python file can either run as main or as a library import:

```bash
$ python3 prog.py # Running as main
```

```python
import prog   # Running as library import
```

In both cases, `__name__` is the name of the module. However, it will only be set to `__main__` if running as main.

Usually, you don't want statements that are part of the main program to execute on a library import. So, it's common to have an `if-`check in code that might be used either way.

```python
if __name__ == '__main__':
    # Does not execute if loaded with import ...
```
