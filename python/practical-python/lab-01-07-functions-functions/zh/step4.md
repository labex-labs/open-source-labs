# 捕获和处理异常

异常可以被捕获和处理。

要进行捕获，可以使用 `try - except` 语句。

```python
for line in file:
    fields = line.split(',')
    try:
        shares = int(fields[1])
    except ValueError:
        print("Couldn't parse", line)
  ...
```

`ValueError` 这个名称必须与你试图捕获的错误类型相匹配。

通常很难预先确切知道根据所执行的操作可能会发生哪些类型的错误。不管是好是坏，异常处理通常是在程序意外崩溃之后才添加的（即“哦，我们忘了捕获那个错误。我们应该处理它！”）。
