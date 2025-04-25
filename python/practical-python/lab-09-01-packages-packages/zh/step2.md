# 包与模块

对于更大的代码集合，将模块组织成包是很常见的做法。

```code
# 从这样
pcost.py
report.py
fileparse.py

# 到这样
porty/
    __init__.py
    pcost.py
    report.py
    fileparse.py
```

你选择一个名称并创建一个顶级目录。上面示例中的 `porty`（显然，选择这个名称是最重要的第一步）。

在该目录中添加一个 `__init__.py` 文件。它可以是空的。

将你的源文件放入该目录中。
