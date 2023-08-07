# Futures

Sometimes Python code executes concurrently via threads or processes. To illustrate, try this example:

```python
>>> import time
>>> def worker(x, y):
        print('About to work')
        time.sleep(20)
        print('Done')
        return x + y

>>> worker(2, 3)     # Normal function call
About to work
Done
5
>>>
```

Now, launch `worker()` into a separate thread:

```python
>>> import threading
>>> t = threading.Thread(target=worker, args=(2, 3))
>>> t.start()
About to work
>>>
Done
```

Carefully notice that the result of the calculation appears nowhere. Not only that, you don't even know when it's going to be completed. There is a certain coordination problem here. The convention for handling this case is to wrap the result of a function in a `Future`. A `Future` represents a future result. Here's how it works:

```python
>>> from concurrent.futures import Future
>>> # Wrapper around the function to use a future
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

You'll see this kind of pattern a lot of if working with thread pools, processes, and other constructs. For example:

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
