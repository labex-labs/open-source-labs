# Problem: Main Scripts

Running a package submodule as a main script breaks.

```bash
$ python porty/pcost.py # BREAKS
...
```

_Reason: You are running Python on a single file and Python doesn't see the rest of the package structure correctly (`sys.path` is wrong)._

All imports break. To fix this, you need to run your program in a different way, using the `-m` option.

```bash
$ python -m porty.pcost # WORKS
...
```
