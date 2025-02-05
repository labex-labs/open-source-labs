# 读取投资组合

在你的`stock.py`程序中添加一个函数`read_portfolio()`，该函数将投资组合数据文件读取到`Stock`对象列表中。其工作方式如下：

```python
>>> portfolio = read_portfolio('portfolio.csv')
>>> for s in portfolio:
        print(s)

<__main__.Stock object at 0x3902f0>
<__main__.Stock object at 0x390270>
<__main__.Stock object at 0x390330>
<__main__.Stock object at 0x390370>
<__main__.Stock object at 0x3903b0>
<__main__.Stock object at 0x3903f0>
<__main__.Stock object at 0x390430>
>>>
```

你在练习2.3中已经编写了一个类似的函数。设计讨论：`read_portfolio()`应该是一个单独的函数还是类定义的一部分？

## 注意：

在`stock.py`文件中添加`read_portfolio()`函数。
