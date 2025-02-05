# `#!` 行

在Unix系统上，`#!` 行可以将脚本作为Python程序来启动。将以下内容添加到脚本文件的第一行。

```python
#!/usr/bin/env python3
#./prog.py
...
```

这需要可执行权限。

```bash
$ chmod +x prog.py
# 然后你就可以执行
$./prog.py
... 输出...
```

**注意：Windows上的Python启动器也会查找 `#!` 行来指示语言版本。**
