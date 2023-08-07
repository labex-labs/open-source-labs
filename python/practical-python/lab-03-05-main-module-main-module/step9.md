# Environment Variables

Environment variables are set in the shell.

```bash
$ setenv NAME dave
$ setenv RSH ssh
$ python3 prog.py
```

`os.environ` is a dictionary that contains these values.

```python
import os

name = os.environ['NAME'] # 'dave'
```

Changes are reflected in any subprocesses later launched by the program.
