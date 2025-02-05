# 未来对象（Futures）

有时，Python 代码会通过线程或进程并发执行。为了说明这一点，试试这个例子：

```python
>>> import time
>>> def worker(x, y):
        print('About to work')
        time.sleep(20)
        print('Done')
        return x + y

>>> worker(2, 3)     # 正常函数调用
About to work
Done
5
>>>
```

现在，将 `worker()` 放入一个单独的线程中：

```python
>>> import threading
>>> t = threading.Thread(target=worker, args=(2, 3))
>>> t.start()
About to work
>>>
Done
```

仔细注意，计算结果 nowhere 出现。不仅如此，你甚至不知道它什么时候会完成。这里存在一定的协调问题。处理这种情况的约定是将函数的结果包装在一个 `Future` 中。一个 `Future` 代表一个未来的结果。它的工作方式如下：

```python
>>> from concurrent.futures import Future
>>> # 围绕函数的包装器，以使用未来对象
>>> def do_work(x, y, fut):
        fut.set_result(worker(x,y))

>>> fut = Future()
>>> t = threading.Thread(target=do_work, args=(2, 3, fut))
>>> t.start()
About to work
>>> result = fut.result()
Done
>>> result
5
>>>
```

如果你使用线程池、进程和其他结构，会经常看到这种模式。例如：

```python
>>> from concurrent.futures import ThreadPoolExecutor
>>> pool = ThreadPoolExecutor()
>>> fut = pool.submit(worker, 2, 3)
About to work
>>> fut
<Future at 0x102157080 state=running>
>>> fut.result()
Done
5
>>>
```

注：原文中“计算结果 nowhere 出现”，nowhere 表述有误，可能是想表达“没有出现”，这里按推测翻译。
