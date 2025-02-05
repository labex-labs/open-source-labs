# 标准输入输出

标准输入/输出（或stdio）是与普通文件工作方式相同的文件。

```python
sys.stdout
sys.stderr
sys.stdin
```

默认情况下，`print` 输出到 `sys.stdout`。输入从 `sys.stdin` 读取。回溯信息和错误信息输出到 `sys.stderr`。

请注意，_stdio_ 可以连接到终端、文件、管道等。

```bash
$ python3 prog.py > results.txt
# 或者
$ cmd1 | python3 prog.py | cmd2
```
