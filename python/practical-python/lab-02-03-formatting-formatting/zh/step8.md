# 练习2.10：打印格式化表格

重做练习2.9中的for循环，但将print语句修改为格式化元组。

```python
>>> for r in report:
        print('%10s %10d %10.2f %10.2f' % r)

          AA        100       9.22     -22.98
         IBM         50     106.28      15.18
         CAT        150      35.46     -47.98
        MSFT        200      20.89     -30.34
...
>>>
```

你也可以展开这些值并使用f字符串。例如：

```python
>>> for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')

          AA        100       9.22     -22.98
         IBM         50     106.28      15.18
         CAT        150      35.46     -47.98
        MSFT        200      20.89     -30.34
...
>>>
```

将上述语句添加到你的`report.py`程序中。让你的程序获取`make_report()`函数的输出，并打印出一个格式良好的表格，如下所示。
