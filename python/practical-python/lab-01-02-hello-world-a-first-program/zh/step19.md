# 练习 1.6：调试

以下代码片段包含了西尔斯大厦问题的代码。其中也存在一个错误。

```python
# sears.py

bill_thickness = 0.11 * 0.001    # 米（0.11 毫米）
sears_height   = 442             # 高度（米）
num_bills      = 1
day            = 1

while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day = days + 1
    num_bills = num_bills * 2

print('天数', day)
print('纸张数', num_bills)
print('最终高度', num_bills * bill_thickness)
```

将上述代码复制并粘贴到一个名为 `sears.py` 的新程序中。当你运行这段代码时，将会得到一个错误消息，导致程序崩溃，如下所示：

```code
Traceback (most recent call last):
  File "sears.py", line 10, in <module>
    day = days + 1
NameError: name 'days' is not defined
```

阅读错误消息是 Python 编程的一个重要部分。如果你的程序崩溃了，回溯消息的最后一行就是程序崩溃的实际原因。在这之上，你应该会看到一段源代码片段，然后是一个标识文件名和行号。

- 错误出在哪一行？
- 错误是什么？
- 修复错误
- 成功运行程序
