# The `#!` line

On Unix, the `#!` line can launch a script as Python. Add the following to the first line of your script file.

```python
#!/usr/bin/env python3
# prog.py
...
```

It requires the executable permission.

```bash
$ chmod +x prog.py
# Then you can execute
$ prog.py
... output ...
```

_Note: The Python Launcher on Windows also looks for the `#!` line to indicate language version._
