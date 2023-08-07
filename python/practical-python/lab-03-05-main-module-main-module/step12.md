# Script Template

Finally, here is a common code template for Python programs that run as command-line scripts:

```python
#!/usr/bin/env python3
# prog.py

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
