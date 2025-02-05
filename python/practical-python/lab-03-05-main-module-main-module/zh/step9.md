# 环境变量

环境变量在 shell 中设置。

```bash
$ export NAME=dave
$ export RSH=ssh
$ python3 prog.py
```

`os.environ` 是一个包含这些值的字典。

```python
import os

name = os.environ['NAME'] # 'dave'
```

程序随后启动的任何子进程都会反映这些更改。
