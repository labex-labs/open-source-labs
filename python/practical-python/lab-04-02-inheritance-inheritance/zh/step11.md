# 多重继承

你可以通过在类的定义中指定多个类来实现多重继承。

```python
class Mother:
 ...

class Father:
 ...

class Child(Mother, Father):
 ...
```

类 `Child` 继承了父母双方的特性。这里有一些相当棘手的细节。除非你清楚自己在做什么，否则不要这样做。下一节会给出一些更多信息，但在本课程中我们不会进一步使用多重继承。

继承的一个主要用途是编写旨在以各种方式进行扩展或定制的代码 —— 特别是在库或框架中。为了说明这一点，看看你 `report.py` 程序中的 `print_report()` 函数。它应该如下所示：

```python
def print_report(reportdata):
    '''
    从 (name, shares, price, change) 元组列表中打印一个格式良好的表格。
    '''
    headers = ('Name','Shares','Price','Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-'*10 + ' ')*len(headers))
    for row in reportdata:
        print('%10s %10d %10.2f %10.2f' % row)
```

当你运行你的报告程序时，你应该会得到如下输出：

```python
>>> import report
>>> report.portfolio_report('portfolio.csv', 'prices.csv')
      Name     Shares      Price     Change
---------- ---------- ---------- ----------
        AA        100       9.22     -22.98
       IBM         50     106.28      15.18
       CAT        150      35.46     -47.98
      MSFT        200      20.89     -30.34
        GE         95      13.48     -26.89
      MSFT         50      20.89     -44.21
       IBM        100     106.28      35.84
```
