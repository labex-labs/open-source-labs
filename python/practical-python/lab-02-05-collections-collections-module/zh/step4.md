# 示例：记录历史

问题：我们想要记录最近N件事情的历史。解决方案：使用 `deque`。

```python
from collections import deque

history = deque(maxlen=N)
with open(filename) as f:
    for line in f:
        history.append(line)
     ...
```

`collections` 模块可能是处理诸如制表和索引等特殊用途数据处理问题最有用的库模块之一。

在本练习中，我们将看几个简单的示例。首先运行你的 `report.py` 程序，以便在交互模式下加载股票投资组合。

```bash
$ python3 -i report.py
```
