# 重新开始

创建一个新文件`stock.py`（或者删除你之前的所有代码）。通过如下方式定义`Stock`来重新开始：

```python
# stock.py

from structure import Structure

class Stock(Structure):
    _fields = ('name','shares', 'price')

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
```

完成此操作后，运行你的`teststock.py`单元测试。你应该会得到很多失败的结果，但至少应该有一些测试会通过。
