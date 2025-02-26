# Шаблон скрипта

Наконец, вот общий шаблон кода для Python-программ, которые запускаются как командные строки:

```python
#!/usr/bin/env python3
#./prog.py

# Import statements (libraries)
import modules

# Functions
def spam():
  ...

def blah():
  ...

# Main function
def main(argv):
    # Parse command line args, environment, etc.
  ...

if __name__ == '__main__':
    import sys
    main(sys.argv)
```
