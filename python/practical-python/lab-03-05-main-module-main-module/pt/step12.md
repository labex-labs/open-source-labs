# Modelo de Script

Finalmente, aqui está um modelo de código comum para programas Python que são executados como scripts de linha de comando:

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
