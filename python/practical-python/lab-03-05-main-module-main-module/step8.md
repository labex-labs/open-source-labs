# Standard I/O

Standard Input / Output (or stdio) are files that work the same as normal files.

```python
sys.stdout
sys.stderr
sys.stdin
```

By default, print is directed to `sys.stdout`. Input is read from `sys.stdin`. Tracebacks and errors are directed to `sys.stderr`.

Be aware that _stdio_ could be connected to terminals, files, pipes, etc.

```bash
$ python3 prog.py > results.txt
# or
$ cmd1 | python3 prog.py | cmd2
```
