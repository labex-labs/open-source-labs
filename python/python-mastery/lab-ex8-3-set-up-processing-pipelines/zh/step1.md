# 一个协程示例

开始使用协程可能有点棘手。下面是一个示例程序，它执行与练习8.2相同的任务，但使用了协程。将此程序复制到一个名为 `cofollow.py` 的文件中。

```python
# cofollow.py
import os
import time

# 数据源
def follow(filename,target):
    with open(filename,'r') as f:
        f.seek(0,os.SEEK_END)
        while True:
            line = f.readline()
            if line!= '':
                target.send(line)
            else:
                time.sleep(0.1)

# 协程函数的装饰器
from functools import wraps

def consumer(func):
    @wraps(func)
    def start(*args,**kwargs):
        f = func(*args,**kwargs)
        f.send(None)
        return f
    return start

# 示例协程
@consumer
def printer():
    while True:
        item = yield     # 接收发送给我的一个项
        print(item)

# 示例用法
if __name__ == '__main__':
    follow('stocklog.csv',printer())
```

运行此程序并确保产生输出。确保你理解不同部分是如何连接在一起的。
