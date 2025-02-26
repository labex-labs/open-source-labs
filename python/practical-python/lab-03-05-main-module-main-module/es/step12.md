# Plantilla de script

Finalmente, aquí está una plantilla de código común para los programas de Python que se ejecutan como scripts de línea de comandos:

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
