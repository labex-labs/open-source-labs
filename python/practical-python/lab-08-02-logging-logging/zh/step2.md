# 重温异常

在练习中，我们编写了一个名为 `parse()` 的函数，大致如下：

```python
# fileparse.py
def parse(f, types=None, names=None, delimiter=None):
    records = []
    for line in f:
        line = line.strip()
        if not line: continue
        try:
            records.append(split(line,types,names,delimiter))
        except ValueError as e:
            print("无法解析 :", line)
            print("原因 :", e)
    return records
```

关注 `try-except` 语句。在 `except` 块中你应该做什么？

你应该打印一条警告消息吗？

```python
try:
    records.append(split(line,types,names,delimiter))
except ValueError as e:
    print("无法解析 :", line)
    print("原因 :", e)
```

还是默默地忽略它？

```python
try:
    records.append(split(line,types,names,delimiter))
except ValueError as e:
    pass
```

这两种解决方案都不尽如人意，因为你通常希望两种行为（用户可选择）都具备。
