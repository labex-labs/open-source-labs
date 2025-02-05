# 改善 Shell 体验

为了改善 Shell 体验，创建一个包含辅助方法的模块（`shelltools.py`），这些方法可以导入到交互式会话中。该模块可以包含用于诸如初始化数据库或删除表等任务的其他辅助方法。

```python
# File: shelltools.py

def initialize_database():
    # 初始化数据库的代码
    pass

def drop_tables():
    # 删除表的代码
    pass
```

在交互式 Shell 中，从 `shelltools` 模块导入所需的方法。

```python
# File: shell.py
# Execution: python shell.py

from shelltools import initialize_database, drop_tables

# 从 shelltools 模块导入所需的方法
from shelltools import *

# 使用导入的方法
initialize_database()
drop_tables()
```
