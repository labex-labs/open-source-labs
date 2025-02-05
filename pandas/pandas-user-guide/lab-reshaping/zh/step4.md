# 交叉制表

交叉制表是一种用于定量分析多个变量之间关系的方法。

```python
# 行与列之间的交叉制表
df.pivot_table(index="row", columns="col", fill_value=0, aggfunc="size")
```
