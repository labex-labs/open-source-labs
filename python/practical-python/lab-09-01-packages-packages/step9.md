# Another solution for scripts

As noted, you now need to use `-m package.module` to
run scripts within your package.

```bash
$ python3 -m porty.pcost portfolio.csv
```

There is another alternative: Write a new top-level script.

```python
#!/usr/bin/env python3
# pcost.py
import porty.pcost
import sys
porty.pcost.main(sys.argv)
```

This script lives _outside_ the package. For example, looking at the directory
structure:

```
pcost.py       # top-level-script
porty/         # package directory
    __init__.py
    pcost.py
    ...
```
