# 延迟求值

考虑这样一个函数：

```python
def after(seconds, func):
    import time
    time.sleep(seconds)
    func()
```

用法示例：

```python
def greeting():
    print('Hello Guido')

after(30, greeting)
```

`after` 会在稍后执行提供的函数。

闭包会携带额外的信息。

```python
def add(x, y):
    def do_add():
        print(f'Adding {x} + {y} -> {x+y}')
    return do_add

def after(seconds, func):
    import time
    time.sleep(seconds)
    func()

after(30, add(2, 3))
# `do_add` 具有对 x -> 2 和 y -> 3 的引用
```
