# 问题：导入

同一包内文件之间的导入**现在必须在导入中包含包名**。记住这个结构。

```code
porty/
    __init__.py
    pcost.py
    report.py
    fileparse.py
```

修改后的导入示例。

```python
from porty import fileparse

def read_portfolio(filename):
    return fileparse.parse_csv(...)
```

所有导入都是**绝对**的，而非相对的。

```python
import fileparse    # 出错。找不到 fileparse

...
```
