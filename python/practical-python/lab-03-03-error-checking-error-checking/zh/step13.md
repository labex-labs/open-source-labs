# `with` 语句

在现代代码中，`try - finally` 通常被 `with` 语句所取代。

```python
lock = Lock()
with lock:
    # 已获取锁
  ...
# 锁已释放
```

一个更常见的例子：

```python
with open(filename) as f:
    # 使用文件
  ...
# 文件已关闭
```

`with` 为资源定义了一个使用 _上下文_。当执行离开该上下文时，资源会被释放。`with` 仅适用于经过专门编程以支持它的某些对象。
