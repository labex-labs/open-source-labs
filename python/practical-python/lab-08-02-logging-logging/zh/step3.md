# 使用日志记录

`logging` 模块可以解决这个问题。

```python
# fileparse.py
import logging
log = logging.getLogger(__name__)

def parse(f,types=None,names=None,delimiter=None):
 ...
    try:
        records.append(split(line,types,names,delimiter))
    except ValueError as e:
        log.warning("无法解析 : %s", line)
        log.debug("原因 : %s", e)
```

代码被修改为使用一个特殊的 `Logger` 对象（通过 `logging.getLogger(__name__)` 创建）来发出警告消息。
