# 添加新方法

向`Stock`类添加一个新方法`sell(nshares)`，该方法通过减少股票数量来卖出一定数量的股票。其工作方式如下：

```python
>>> s = Stock('GOOG',100,490.10)
>>> s.shares
100
>>> s.sell(25)
>>> s.shares
75
>>>
```

## 注意：

在`stock.py`文件中完成`sell(nshares)`函数。
