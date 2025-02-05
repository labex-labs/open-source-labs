# 定位模块

Python 在查找模块时会参考一个路径列表（sys.path）。

```python
>>> import sys
>>> sys.path
[
  '',
  '/usr/local/lib/python36/python36.zip',
  '/usr/local/lib/python36',
...
]
```

当前工作目录通常排在首位。
