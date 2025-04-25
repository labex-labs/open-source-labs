# 生成器管道

你可以利用生成器的这一特性来设置处理管道（类似于 Unix 管道）。

**生产者** → **处理** → **处理** → **消费者**

处理管道有一个初始数据生产者、一些中间处理阶段和一个最终消费者。

**生产者** → **处理** → **处理** → **消费者**

```python
def producer():
  ...
    yield item
  ...
```

生产者通常是一个生成器。不过它也可以是某个其他序列的列表。`yield` 将数据输入到管道中。

**生产者** → **处理** → **处理** → **消费者**

```python
def consumer(s):
    for item in s:
      ...
```

消费者是一个 `for` 循环。它获取项目并对其进行处理。

**生产者** → **处理** → **处理** → **消费者**

```python
def processing(s):
    for item in s:
      ...
        yield newitem
      ...
```

中间处理阶段同时消费和生产项目。它们可能会修改数据流。它们也可以进行过滤（丢弃项目）。

**生产者** → **处理** → **处理** → **消费者**

```python
def producer():
  ...
    yield item          # 生成由 `processing` 接收的项目
  ...

def processing(s):
    for item in s:      # 来自 `producer`
      ...
        yield newitem   # 生成一个新项目
      ...

def consumer(s):
    for item in s:      # 来自 `processing`
      ...
```

设置管道的代码

```python
a = producer()
b = processing(a)
c = consumer(b)
```

你会注意到数据会逐步流经不同的函数。

对于这个练习，`stocksim.py` 程序应该仍在后台运行。你将使用在前一个练习中编写的 `follow()` 函数。
