# 异常处理

异常会传播到第一个匹配的 `except` 块。

```python
def grok():
  ...
    raise RuntimeError('Whoa!')   # 在此处引发异常

def spam():
    grok()                        # 此调用将引发异常

def bar():
    try:
       spam()
    except RuntimeError as e:     # 在此处捕获异常
      ...

def foo():
    try:
         bar()
    except RuntimeError as e:     # 异常不会到达此处
      ...

foo()
```

要处理异常，可在 `except` 块中放置语句。你可以添加任何想要用来处理错误的语句。

```python
def grok():...
    raise RuntimeError('Whoa!')

def bar():
    try:
      grok()
    except RuntimeError as e:   # 在此处捕获异常
        statements              # 使用这些语句
        statements
      ...

bar()
```

处理完异常后，执行会从 `try-except` 之后的第一条语句继续。

```python
def grok():...
    raise RuntimeError('Whoa!')

def bar():
    try:
      grok()
    except RuntimeError as e:   # 在此处捕获异常
        statements
        statements
      ...
    statements                  # 在此处恢复执行
    statements                  # 并在此处继续
  ...

bar()
```
